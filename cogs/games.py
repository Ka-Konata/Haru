import discord
import asyncio

client = discord.Client()

class Cmd_games:
    def __init__(self, message, aliases, prefixo, lang, colors):
        self.message = message
        self.aliases = aliases
        self.prefixo = prefixo
        self.lang    = lang
        self.colors  = colors

    
    # Comando Coin Flip
    @client.event
    async def coinflip(self):
        import random
        lang    = self.lang["COINFLIP"]
        channel = self.message.channel

        num     = random.randint(0, 1)
        coin    = ["cara", "coroa"]

        if not "cara" in self.message.content.lower() and not "coroa" in self.message.content.lower():
            await channel.send(lang["COINFLIP_MISSING_ERROR"] + f"\nexample: `{self.prefixo}coinflip cara`")
        else:
            result = lang["WIN"] if coin[num] in self.message.content.lower().split()[1] else lang["LOSE"]

            if num   == 0:
                await channel.send(lang["COINFLIP_RESULT_CARA"] + f" **{result}**!")
            elif num == 1:
                await channel.send(lang["COINFLIP_RESULT_COROA"] + f" **{result}**!")