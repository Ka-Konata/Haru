import discord
import asyncio
import random

client = discord.Client()

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
        print(message.author.id)
        if message.author.id == 502687173099913216:
            choice = random.randint(1, 2)
            if choice == 1:
                await message.add_reaction("👈")
            if choice == 2:
                await message.add_reaction("👉")

        else:
            await message.channel.send("Você não tem permissão para executar esse comando")

client.run("ODA4MTAwMTk4ODk5Mzg0MzUy.YCBn9Q.nsaNN5PQEX0UfsQtkxr1kcIS4a0")