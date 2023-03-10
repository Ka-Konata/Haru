import discord
from scripts import configs, colors
from random import randint

gifs = {
    'kiss': [
        'https://i.imgur.com/t31KfJa.gif',
        'https://i.imgur.com/XVaEUrm.gif',
        'https://i.imgur.com/5fO55h2.gif',
        'https://i.imgur.com/Q7BR8HW.gif',
        'https://i.imgur.com/xuJIIyJ.gif',
        'https://i.imgur.com/T9iyrdT.gif',
        'https://i.imgur.com/rGXhbrQ.gif',
        'https://i.imgur.com/8wekXG0.gif',
        'https://i.imgur.com/GWbe2XC.gif',
        'https://i.imgur.com/QBgzaYV.gif',
        'https://i.imgur.com/dXfKzPI.gif',
        'https://i.imgur.com/PnPf01M.gif',
        'https://i.imgur.com/rB1yoxY.gif',
        'https://i.imgur.com/gi1voQA.gif',
        'https://i.imgur.com/XzDiXJf.gif',
        'https://i.imgur.com/8eUROrB.gif',
        'https://i.imgur.com/xKjDIO7.gif',
        'https://i.imgur.com/dj1MfB4.gif',
        'https://i.imgur.com/YNyLSpw.gif',
        'https://i.imgur.com/FmB42gO.gif',
        'https://i.imgur.com/3QY9Uhj.gif',
        'https://i.imgur.com/YLBa9IF.gif',
        'https://i.imgur.com/opbAvDs.gif'
    ],
    'dance': [
        'https://i.imgur.com/81mI9Xe.gif',
        'https://i.imgur.com/qAVGFDr.gif',
        'https://i.imgur.com/QjuwqhV.gif',
        'https://i.imgur.com/IXLPWY4.gif',
        'https://i.imgur.com/Wo8CPys.gif',
        'https://i.imgur.com/xrkrcJh.gif',
        'https://i.imgur.com/fUVonjA.gif',
        'https://i.imgur.com/oOLKKgE.gif',
        'https://i.imgur.com/UPR7rSO.gif',
        'https://i.imgur.com/yfVKIET.gif',
        'https://i.imgur.com/m2caT04.gif',
        'https://i.imgur.com/C46wkeD.gif',
        'https://i.imgur.com/h2o2Km3.gif',
        'https://i.imgur.com/bmMxvL8.gif',
        'https://i.imgur.com/YXVFV69.gif'
    ],
    'shoot': [
        'https://i.imgur.com/zh9edDe.gif',
        'https://i.imgur.com/SmhaKa0.gif',
        'https://i.imgur.com/eK9yozO.gif',
        'https://i.imgur.com/L6c7JdL.gif',
        'https://i.imgur.com/nfivRUh.gif',
        'https://i.imgur.com/em35dOM.gif',
        'https://i.imgur.com/OPRk4UT.gif',
        'https://i.imgur.com/1E5mMS5.gif',
        'https://i.imgur.com/gBwNfyp.gif',
        'https://i.imgur.com/ok7DE60.gif',
        'https://i.imgur.com/k1xnsw3.gif',
        'https://i.imgur.com/MQcLNB2.gif'
    ],
    'hug': [
        'https://i.imgur.com/JupEThS.gif',
        'https://i.imgur.com/sknl06j.gif',
        'https://i.imgur.com/8RBOJmg.gif',
        'https://i.imgur.com/RVzS0S9.gif',
        'https://i.imgur.com/qDYr3ia.gif',
        'https://i.imgur.com/2q1Yl9F.gif',
        'https://i.imgur.com/Oz6em0n.gif',
        'https://i.imgur.com/9Pdj3y9.gif',
        'https://i.imgur.com/Xu8gkqt.gif',
        'https://i.imgur.com/RhjIThH.gif',
        'https://i.imgur.com/36MXqpz.gif',
        'https://i.imgur.com/bqXKulm.gif',
        'https://i.imgur.com/KB1F080.gif',
        'https://i.imgur.com/lwz836d.gif',
        'https://i.imgur.com/N5mYkJI.gif',
        'https://i.imgur.com/fnEU49l.gif',
        'https://i.imgur.com/rdnhmHk.gif',
        'https://i.imgur.com/cq7gme3.gif',
        'https://i.imgur.com/hxHW888.gif',
        'https://i.imgur.com/lVyKRQR.gif',
        'https://i.imgur.com/nwOhd6D.gif'
    ],
    'slap': [
        'https://i.imgur.com/97QKVxK.gif',
        'https://i.imgur.com/GHomcpf.gif',
        'https://i.imgur.com/T2l5303.gif',
        'https://i.imgur.com/6YuFhoH.gif',
        'https://i.imgur.com/ExebQH7.gif',
        'https://i.imgur.com/TzLDJtM.gif',
        'https://i.imgur.com/rewB5tg.gif',
        'https://i.imgur.com/684hLY7.gif',
        'https://i.imgur.com/uGqfGjr.gif',
        'https://i.imgur.com/RJk6In3.gif',
        'https://i.imgur.com/C01WX0m.gif',
        'https://i.imgur.com/DzSn23j.gif',
        'https://i.imgur.com/MpShgOI.gif',
        'https://i.imgur.com/DUp9UGS.gif',
        'https://i.imgur.com/ISR9pAB.gif',
        'https://i.imgur.com/eSKdAW0.gif',
        'https://i.imgur.com/Ax3XdJv.gif',
        'https://i.imgur.com/GBJpdZm.gif',
        'https://i.imgur.com/AZb0eIV.gif',
        'https://i.imgur.com/G1QSM2X.gif',
        'https://i.imgur.com/zZZjC8v.gif'
    ],
    'pat': [
        'https://i.imgur.com/mVBj2jd.gif',
        'https://i.imgur.com/zIDU2Au.gif',
        'https://i.imgur.com/mSW6v6P.gif',
        'https://i.imgur.com/zNHkEb1.gif',
        'https://i.imgur.com/9JsR3OP.gif',
        'https://i.imgur.com/2A5TcFZ.gif',
        'https://i.imgur.com/AXgACFC.gif',
        'https://i.imgur.com/9BMeSRy.gif',
        'https://i.imgur.com/3GWc3y2.gif',
        'https://i.imgur.com/p5J02FE.gif',
        'https://i.imgur.com/xE59VGl.gif',
        'https://i.imgur.com/AnOLKy1.gif',
        'https://i.imgur.com/RpASJP8.gif',
        'https://i.imgur.com/fUWBkbu.gif',
        'https://i.imgur.com/wDY32zU.gif'

    ],
    'lick': [
        "https://i.imgur.com/Kzi5OHg.gif",
        "https://i.imgur.com/pARxiXM.gif",
        'https://i.imgur.com/7jnxb5m.gif',
        'https://i.imgur.com/s0vJLGC.gif',
        'https://i.imgur.com/shdbdc3.gif',
        'https://i.imgur.com/Igc4b65.gif',
        'https://i.imgur.com/vOtlBMo.gif',
        'https://i.imgur.com/sDK5VZZ.gif',
        'https://i.imgur.com/XmOmsny.gif',
        'https://i.imgur.com/FKj8dwi.gif',
        'https://i.imgur.com/XJIYCjs.gif'
    ],
    'bite': [
        'https://i.imgur.com/XfnJ5TP.gif',
        'https://i.imgur.com/mQgD3lO.gif',
        'https://i.imgur.com/0YB67fv.gif',
        'https://i.imgur.com/AclwRAK.gif',
        'https://i.imgur.com/5TIaaxs.gif',
        'https://i.imgur.com/NRIRrRB.gif',
        'https://i.imgur.com/IViizVa.gif',
        'https://i.imgur.com/ulnRcDI.gif',
        'https://i.imgur.com/T3nzVVr.gif',
        'https://i.imgur.com/EWEsV1W.gif',
        'https://i.imgur.com/ihRX1eG.gif',
        'https://i.imgur.com/3U35kwq.gif'
    ]
}


def generate(type: str, lang: dict, settings: dict, user1, user2):
    title = user1.mention + lang['COMMAND'][type.upper()]['TITLE'] + user2.mention

    choice = randint(0, len(gifs[type]) - 1)
    embed = discord.Embed(color=colors.default)
    embed.set_image(url=gifs[type][choice])
    embed.set_author(name=lang['COMMAND'][type.upper()]['NAME'], icon_url=settings['bot-icon'])
    embed.set_footer(text=lang['COMMAND'][type.upper()]['FOOTER'])
    return {'embed':embed, 'title':title}