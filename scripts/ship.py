import discord
import asyncio
import requests
from PIL               import Image
from random            import shuffle
from io                import BytesIO
from os                import remove, path

intents = discord.Intents.default()
intents.members = True

client  = discord.Client(intents=intents)
Thistle	= 0xD8BFD8	

@client.event
async def get_couple(users, toPNG, channel, message):

    id0 = users[0].id % 100
    id1 = users[1].id % 100

    percentage = id0 + id1

    if percentage > 100:
        percentage = percentage % 100

    percentage = str(percentage)

    arq  = "assets/ships" + str(users[0].id) + "+" + str(users[1].id) + ".png"
    arq1 = str(users[0].id) + "+" + str(users[1].id) + ".png"

    if users[0].is_avatar_animated():
        url0      = requests.get(users[0].avatar_url_as(format="gif"))
        avatar0   = Image.open(BytesIO(url0.content))
        filename  = "assets/avatar" + str(users[0].id) + ".gif"

        avatar0.save(filename)

        filename0 = toPNG(filename)
        avatar0   = Image.open(filename0)

        remove(filename)

    else:
        url0      = requests.get(users[0].avatar_url_as(format="png"))
        avatar0   = Image.open(BytesIO(url0.content))
        filename0 = "assets/avatar" + str(users[0].id) + ".png"


    if users[1].is_avatar_animated():
        url1      = requests.get(users[1].avatar_url_as(format="gif"))
        avatar1   = Image.open(BytesIO(url1.content))
        filename  = "assets/avatar" + str(users[1].id) + ".gif"

        avatar1.save(filename)

        filename1 = toPNG(filename)
        avatar1   = Image.open(filename1)

        remove(filename)

    else:
        url1      = requests.get(users[1].avatar_url_as(format="png"))
        avatar1   = Image.open(BytesIO(url1.content))
        filename1 = "assets/avatar" + str(users[1].id) + ".png"

    basename      = Image.open("assets/ships.png")

    avatar0       = avatar0.resize((130, 130))
    avatar1       = avatar1.resize((130, 130))

    basename.paste(avatar0, (0, 0))
    basename.paste(avatar1, (128, 0))
    basename.save("assets/ships" + str(users[0].id) + "+" + str(users[1].id) + ".png")

    with open(arq, "rb") as fp:
        await channel.send(file=discord.File(fp, arq1))

    title = "`[]"
    for n in range(0, int(percentage)//10):
        title = title + "="
        n = n + 1 - 1
    title = title + ">` **" + percentage + "%**"

    author_name = users[0].name + " & " + users[1].name

    while True:
        last_msg_id  = channel.last_message_id
        last_msg     = await channel.fetch_message(last_msg_id)
        if last_msg.attachments[0].filename == str(users[0].id) + str(users[1].id) + ".png":
            break

    embed = discord.Embed(title=title, color=Thistle)
    embed.set_author(name=author_name)
    embed.set_image(url=last_msg.attachments[0].url)
    await message.reply(embed=embed)

    remove(arq)
