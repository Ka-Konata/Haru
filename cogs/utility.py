import discord
import asyncio

client = discord.Client()

class Cmd_utility:
    def __init__(self, message, aliases, prefixo, lang, colors):
        self.message = message
        self.aliases = aliases
        self.prefixo = prefixo
        self.lang    = lang
        self.colors  = colors

    # Comando Morse
    @client.event
    async def morse(self, morse_códigos):
        import random
        lang    = self.lang["MORSE"]
        channel = self.message.channel

        if len(self.message.content.split()) < 2:
            await channel.send(lang["MORSE_MISSING_ERROR"] + f"\nexample: `{self.prefixo}morse My name is Haru`")
        else:
            description = "**"
            frase = self.message.content.lower().split()[1:]

            for n, word in enumerate(frase):
                breakl = False
                word = list(word)
                for n2, letter in enumerate(word):

                    try:
                        description = description + morse_códigos[letter] + " "
                    except KeyError:
                        await channel.send(lang["MORSE_UNKNOWN_CHARACTER_ERROR"])
                        breakl = True
                        break

                    if n2 == len(word) - 1 and n < len(frase) - 1:
                        description = description + "/ "

                if breakl:
                    break
                elif n == len(frase) - 1:
                    description = description + "**"
                    embed_msg = discord.Embed(title=lang["MORSE_TRANSLATED_TITLE"], color=self.colors.Thistle, description=description)
                    await channel.send(embed=embed_msg)


    # Comando Invite
    @client.event
    async def invite(self):
        lang = self.lang["INVITE"]

        permissions = "8"
        bot_id      = "808100198899384352"
        invite      = "https://discord.com/oauth2/authorize?client_id=" + bot_id + "&scope=bot&permissions=" + permissions

        await self.message.reply(lang["INVITE_MSG"] + "\n" + invite)