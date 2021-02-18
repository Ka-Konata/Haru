import discord
import asyncio

client = discord.Client()

class Cmd_fun:
    def __init__(self, message, aliases, lang, colors, prefixo, help):
        self.message = message
        self.aliases = aliases
        self.lang    = lang
        self.colors  = colors
        self.prefixo = prefixo
        self._help    = help


    # Comando Say
    @client.event
    async def say(self):
        if len(self.message.content.split()) > 1:
            msg = ""
            for n, word in enumerate(self.message.content.split()):
                if n > 0:
                    msg = msg + " " + word

            await self.message.channel.send(msg)
            await self.message.delete()
        else:
            self._help.help("say")