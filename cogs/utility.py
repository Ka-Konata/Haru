import discord
import asyncio

client = discord.Client()

class Cmd_utility:
    def __init__(self):
        pass    

    # Comando Morse
    @client.event
    async def morse(self, message, prefixo, lang, morse_códigos, colors):
        import random
        lang    = lang["MORSE"]
        channel = message.channel

        if len(message.content.split()) < 2:
            await channel.send(lang["MORSE_MISSING_ERROR"] + f"\nexample: `{prefixo}morse My name is Haru`")
        else:
            description = "**"
            frase = message.content.lower().split()[1:]

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
                    embed_msg = discord.Embed(title=lang["MORSE_TRANSLATED_TITLE"], color=colors.Thistle, description=description)
                    await channel.send(embed=embed_msg)