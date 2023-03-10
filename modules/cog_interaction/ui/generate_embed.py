import discord
from scripts import configs, colors
from random import randint

gifs = {
    'kiss': [
        'https://i.imgur.com/t31KfJa.gif',
        'https://i.imgur.com/XVaEUrm.gif',
        'https://i.imgur.com/5fO55h2.gif',
        'https://i.imgur.com/Q7BR8HW.gif'
        'https://i.imgur.com/xuJIIyJ.gif',
        'https://i.imgur.com/agCLNMP.gif',
        'https://i.imgur.com/T9iyrdT.gif'
    ]
}


def generate(type: str, lang: dict, settings: dict, user1, user2):
    title = user1.mention + lang['COMMAND']['KISS']['TITLE'] + user2.mention

    choice = randint(0, len(gifs[type]) - 1)
    embed = discord.Embed(color=colors.default)
    embed.set_image(url=gifs[type][choice])
    embed.set_author(name=lang['COMMAND'][type.upper()]['NAME'], icon_url=settings['bot-icon'])
    embed.set_footer(text=lang['COMMAND'][type.upper()]['FOOTER'])
    return {'embed':embed, 'title':title}