import discord
import asyncio
import random
from sys import exit
import bot_token.secret_token as token

client = discord.Client()
TOKEN  = token.get_token()  # Make your file with your token

@client.event
async def on_ready():
    print("BOT ONLINE - HELLO WORLD")
    print(client.user.name)
    print(client.user.id)
    print("-------------------------")


@client.event
async def on_message(message):
    if message.content.lower().startswith("?test"):
        channel = message.channel
        await channel.send("Hello world, I'm alive.")

    
    if message.content.lower().startswith("?coinflip"):
        if message.author.id == 502687173099913216:
            choice = random.randint(1, 2)
            if choice == 1:
                await message.add_reaction("👈")
            if choice == 2:
                await message.add_reaction("👉")

        else:
            await message.channel.send("Você não tem permissão para executar esse comando")

    if message.content.lower().startswith("?stoprunning"):
        if message.author.id == 502687173099913216:
            await message.channel.send("Encerrando o programa.")
            print("Encerrando o programa.")
            exit()
            
        
        else:
            await message.channel.send("Você não tem permissão para executar esse comando")

client.run(TOKEN)