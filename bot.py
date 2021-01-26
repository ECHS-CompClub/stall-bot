import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="~")

def codeblock(string):
    string = f"```{string}```"

    return string

@client.event
async def on_ready():
    print("Bot is Active.")

@client.command()
async def ping(ctx):
    await ctx.send(codeblock(f"Pong! {round(client.latency * 1000)}ms"))

@client.command()
async def ls(ctx, path="./"):
    output = ""
    for file in os.listdir(path):
        output += f"{file}\n"
        
    await ctx.send(codeblock(output))

@client.command()
async def cat(ctx, path):
    contents = open(path)
    await ctx.send(codeblock(contents.read()))



client.run("BOT_TOKEN_HERE")
