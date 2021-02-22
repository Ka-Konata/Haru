import discord
import asyncio
import random
from scripts           import ship
from sys               import exit
from utils.usual       import Utils
from utils             import morse
from scripts           import aliases, requeriments
from scripts.format    import toPNG
from scripts.bot_token import secret_token as token

morse_códigos = morse.get_morse()
icon_url = "https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif"


intents = discord.Intents.default()
intents.members = True

client  = discord.Client(intents=intents)
TOKEN   = token.get_token()  # Make your file with your token
prefixo = ";"
utils   = Utils(icon_url)

# Cores color
from scripts import colors

guild    = None
msg_id   = None
msg_user = None


@client.event
async def on_ready():
    channel = client.get_channel(788785603105259574)
    embed_msg = discord.Embed(title="BOT ONLINE - HELLO WORLD", color=colors.ciano, description=f"**Bot UserName:**  {client.user.name} \n**Bot UserID:**  {client.user.id} \n**Channel:**  {channel.mention}")
    await channel.send(embed=embed_msg)
    print("BOT ONLINE - HELLO WORLD")
    print(client.user.name)
    print(client.user.id)
    print("-------------------------")


@client.event
async def on_message(message):
    if message.channel.id == 788785603105259574:
        channel_send = client.get_channel(788785603105259574)
        channel = client.get_channel(810690029847969833)

        last_msg_id  = channel.last_message_id
        last_msg     = await channel.fetch_message(last_msg_id)
            
        embed = discord.Embed(title="o ship..")
        print(last_msg.attachments[0].url)
        embed.set_image(url=last_msg.attachments[0].url)
        await channel_send.send(embed=embed)


client.run(TOKEN)