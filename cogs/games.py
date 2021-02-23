import discord
import asyncio

client = discord.Client()

class Cmd_games:
    def __init__(self, message, aliases, prefixo, lang, colors, help):
        self.message = message
        self.aliases = aliases
        self.prefixo = prefixo
        self.lang    = lang
        self.colors  = colors
        self._help   = help

    
    # Comando Coin Flip
    @client.event
    async def coinflip(self):
        from random import randint
        lang    = self.lang["COINFLIP"]
        channel = self.message.channel

        num     = randint(0, 1)
        coin    = ["cara", "coroa"]

        if not "cara" in self.message.content.lower() and not "coroa" in self.message.content.lower():
            await channel.send(lang["COINFLIP_MISSING_ERROR"] + f"\nexample: `{self.prefixo}coinflip cara`")
        else:
            result = lang["WIN"] if coin[num] in self.message.content.lower().split()[1] else lang["LOSE"]

            if num   == 0:
                await channel.send(lang["COINFLIP_RESULT_CARA"] + f" **{result}**!")
            elif num == 1:
                await channel.send(lang["COINFLIP_RESULT_COROA"] + f" **{result}**!")

    
    @client.event
    async def dice(self):
        from random import randint
        lang    = self.lang["DICE"]
        content = self.message.content.split()
        lados   = 6

        if len(content) > 1:
            try:
                lados = int(content[1])
            except ValueError:
                self._help.help(request="dice")
        else:
            lados = 6

        choice = randint(0, lados)
        await self.message.reply("🎲| " + self.message.author.mention + lang["ROLLING"] + "**" + str(lados) + "**" + lang["RESULT"] + "**" + str(choice) + "!**")
