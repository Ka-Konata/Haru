import discord
import asyncio


intents = discord.Intents.default()
intents.members = True

client  = discord.Client(intents=intents)

class Cmd_fun:
    def __init__(self, message, client, aliases, lang, colors, prefixo, help, mentions):
        self.message  = message
        self.aliases  = aliases
        self.lang     = lang
        self.colors   = colors
        self.prefixo  = prefixo
        self._help    = help
        self.mentions = mentions 
        self.client   = client


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
            await self._help.help("say")

    
    # Comando Send
    @client.event
    async def send(self):
        content = self.message.content.split()
        lang = self.lang["SEND"]
        if len(content) > 2:
            if len(self.mentions) == 0:
                try:
                    user_tosend = self.client.get_user(int(content[1]))
                except ValueError:
                    await self.message.channel.send(lang["USER_NOT_FOUND_ERROR"] + "`" + content[1] + "`.")
            else: 
                user_tosend = self.mentions[0]
            msg_tosend = ""
            for n, word in enumerate(content):
                if n > 1:
                    msg_tosend = msg_tosend + word + " "
            try: 
                await user_tosend.send(msg_tosend)
            except discord.errors.Forbidden:
                await self.message.channel.send(lang["COULDNT_SEND"])
        else:
            await self._help.help("send")