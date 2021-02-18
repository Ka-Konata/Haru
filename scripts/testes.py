import discord
import asyncio

client  = discord.Client()
TOKEN   = "ODA4MTAwMTk4ODk5Mzg0MzUy.YCBn9Q.nt-bLFn99uehXhWOiLEoWarsvgE"
prefixo = "?"

guild    = None
color    = 0x8E44AD
msg_id   = None
msg_user = None

@client.event
async def on_ready():
    channel = client.get_channel(788785603105259574)
    await channel.send("BOT ONLINE - HELLO WORLD")
    print("BOT ONLINE - HELLO WORLD")

@client.event
async def function():
    pass

client.run(TOKEN)