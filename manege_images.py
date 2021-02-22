import discord
import importlib
import asyncio
from scripts.bot_token import secret_token as token
from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
from scripts import colors
from io  import BytesIO
from os  import remove
from scripts.format import toPNG

intents = discord.Intents.default()
intents.members = True

client  = discord.Client(intents=intents)
TOKEN   = token.get_token()  # Make your file with your token

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
    if message.guild.id == 803997027733471242 and message.author.id != 808100198899384352:

        user   = client.get_user(message.author.id)
        print(message.author.name, user.is_avatar_animated())
        if user.is_avatar_animated():
            url       = requests.get(user.avatar_url_as(format="gif"))
            avatar    = Image.open(BytesIO(url.content))
            filename1 = "arquivos/avatar" + str(message.author.id) + ".gif"
            avatar.save(filename1)
            filename  = toPNG(filename1)
            print(filename)
            avatar    = Image.open(filename)
            remove(filename1)
            
        else:
            url       = requests.get(user.avatar_url_as(format="png"))
            avatar    = Image.open(BytesIO(url.content))
            filename  = "arquivos/avatar" + str(message.author.id) + ".png"
        print(user.avatar_url_as(format="png"))

        avatar    = avatar.resize((130, 130))
        bigavatar = (avatar.size[0] * 3, avatar.size[1] * 3)
        mascara   = Image.new("L", bigavatar, 0)
        recortar  = ImageDraw.Draw(mascara)
        recortar.ellipse((0, 0) + bigavatar, fill=255)
        mascara   = mascara.resize(avatar.size, Image.ANTIALIAS)
        avatar.putalpha(mascara)

        saida     = ImageOps.fit(avatar, mascara.size, centering=(0.5, 0.5))
        saida.putalpha(mascara)
        saida.save("arquivos/avatar" + str(message.author.id) + ".png")

        avatar    = Image.open(filename)
        fundo     = Image.open('arquivos/bemvindo.png')
        fonte     = ImageFont.truetype("arquivos/BebasNeue.ttf", 50)
        escrever  = ImageDraw.Draw(avatar)
        escrever.text(xy=(200, 171), text=message.author.name, fill=(255,0,0), font=fonte)
        fundo.paste(avatar, (40, 90), avatar)
        fundo.save('arquivos/bv.png')


        with open('arquivos/bv.png', 'rb') as fp:
            channel = client.get_channel(788785603105259574)
            await channel.send(file=discord.File(fp, 'bv_image.png'))
        print("message sent")


client.run(TOKEN)                                                                