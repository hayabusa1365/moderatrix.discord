import discord
from discord.ext import commands
import random
from config import token

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Successfully logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def about(ctx):
    await ctx.send('This is an echo-bot made with the discord.py library!')

@client.command()
async def kata_kata_hari_ini(ctx):
    await ctx.send('disuruh pilih coklat atau keju, padahal maunya wanna be with you 😌')

@client.command()
async def info(ctx):
    await ctx.send('This bot was created to demonstrate the command feature in discord.py.')

@client.command()
async def alamakk(ctx):
    await ctx.send(file=discord.File('menggoda.jpg'))

client.run(token)
