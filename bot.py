import discord
from discord.ext import commands
from config import TOKEN
from password_generator import generate_password
from random import choice
import random

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return
    if message.content.startswith('Hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('Bye!'):
        await message.channel.send("Bye!")
    await bot.process_commands(message)


@bot.command()
async def coin(ctx: commands.Context):
    result = choice(["Орел", "Решка"])
    await ctx.send(result)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command()
async def password(ctx: commands.Context, length=5):
    new_password = generate_password(length)
    print(new_password)
    await ctx.send(new_password)


bot.run(TOKEN)
