import discord
import asyncio

client = discord.Client()

class Cmd_utility:
    def __init__(self, message, aliases, prefixo, lang, colors, help, _client):
        self.message = message
        self.aliases = aliases
        self.prefixo = prefixo
        self.lang    = lang
        self.colors  = colors
        self._help   = help
        self.client  = _client

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

    
    # Comando flipmsg
    @client.event
    async def flipmsg(self):
        content = self.message.content.split()

        if len(content) > 1:
            new_content = ""
            for word in content[1:]:
                for letter in word:
                    new_content = letter + new_content
                new_content = " " + new_content

            await self.message.reply(new_content)

        else:
            self._help.help(request="flipmsg") 

    # Comando avatar
    @client.event
    async def avatar(self):
        lang    = self.lang["AVATAR"]
        error   = False
        content = self.message.content.split()

        if len(content) > 1:
            try:
                user    = self.client.get_user(int(content[1]))
                user.id = user.id
                url = user.avatar_url
            except (ValueError, AttributeError) as erro:
                print(erro)
                try:
                    user = self.message.mentions[0]
                    url = user.avatar_url
                except IndexError as erro:
                    print(erro)
                    error = True
                    await self.message.channel.send(lang["USER_NOT_FOUND_ERROR"] + "`" + content[1] + "`")
        else:
            url = self.message.author.avatar_url
        if not error:
            embed = discord.Embed(title=lang["DOWNLAOD_IMG"], url=str(url), color=self.colors.Thistle)
            embed.set_author(name=self.message.author.name + "#" + self.message.author.discriminator, icon_url=self.message.author.avatar_url)
            embed.set_image(url=url)
            print("url", url)
            await self.message.reply(embed=embed)
