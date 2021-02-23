import discord
import asyncio
import random


intents = discord.Intents.default()
intents.members = True

client  = discord.Client(intents=intents)

class Cmd_fun:
    def __init__(self, message, client, aliases, lang, colors, prefixo, help, utils, mentions):
        self.message  = message
        self.aliases  = aliases
        self.lang     = lang
        self.colors   = colors
        self.prefixo  = prefixo
        self._help    = help
        self.utils    = utils
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


    # Comando Ship
    @client.event
    async def ship(self, ship, toPNG):
        users   = []
        content = self.message.content.split()
        lang    = self.lang["SHIP"]

        if len(content) > 1:
            num = 0
            error = False
            for n, user in enumerate(content[1:3]):
                try:
                    users.append(self.client.get_user(int(user)))
                    n = users[n].id
                except (ValueError, AttributeError):
                    try:
                        users.append(self.mentions[num])
                        num += 1
                    except IndexError:
                        error = True
                        await self.message.channel.send(lang["USER_NOT_FOUND_ERROR"] + "`" + user + "`")  # send a message error for user not found
                        break
                finally:

                    guild_ast = self.client.get_guild(788518735752724480)
                    assets_ch = guild_ast.get_channel(813497519539617812)

                    if len(content) == 2 and len(users) > 0 and not error:
                        users.append(self.message.author)
                        await ship.get_couple(users, toPNG, assets_ch, self.message)
                        break

                    elif len(content) > 2 and content[1] == content[2] and not error:
                        users.append(users[0])
                        await ship.get_couple(users, toPNG, assets_ch, self.message)
                        break

                    elif len(content) > 2 and len(users) == 2 and not error:
                        await ship.get_couple(users, toPNG, assets_ch, self.message)
        else:
            await self._help.help(request="ship")


    @client.event
    async def kiss(self, gifs, reply=False):
        await self.utils.command_gif(self.message, self.mentions, self.lang, "KISS", self.client, self._help, gifs.kiss, "kiss", reply=reply)


    @client.event
    async def hug(self, gifs, reply=False):
        await self.utils.command_gif(self.message, self.mentions, self.lang, "HUG", self.client, self._help, gifs.hug, "hug", reply=reply)


    @client.event
    async def pat(self, gifs, reply=False):
        await self.utils.command_gif(self.message, self.mentions, self.lang, "PAT", self.client, self._help, gifs.pat, "pat", reply=reply)


    @client.event
    async def slap(self, gifs, reply=False):
        await self.utils.command_gif(self.message, self.mentions, self.lang, "SLAP", self.client, self._help, gifs.slap, "slap", reply=reply)


    @client.event
    async def shoot(self, gifs, reply=False):
        await self.utils.command_gif(self.message, self.mentions, self.lang, "SHOOT", self.client, self._help, gifs.shoot, "shoot", reply=reply)

