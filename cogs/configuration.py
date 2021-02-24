import discord
import asyncio

client = discord.Client()

class Cmd_configuration:
    def __init__(self, message, lang, colors, member_perms, bot_perms, utils, help, prefixo):
        self.message      = message
        self.lang         = lang
        self.colors       = colors
        self.member_perms = member_perms
        self.utils        = utils
        self.help         = help
        self.prefixo      = prefixo

    # Comando Set Language
    @client.event
    async def setlanguage(self):
        lang    = self.lang["SETLANGUAGE"]
        channel = self.message.channel
        guild   = self.message.guild
        langs   = ("en", "pt_BR")

        if len(self.message.content.split()) > 1 and self.message.content.split()[1] in langs:

            if self.member_perms.admin:
                content = self.utils.open_json("languages/guild_languages.json")
                content[str(guild.id)] = self.message.content.split()[1]

                self.utils.write_json("languages/guild_languages.json", content)
                lang  = self.utils.set_language(self.prefixo, str(self.message.guild.id))["SETLANGUAGE"]

                embed = discord.Embed(title=self.message.content.split()[1], color=self.colors.Thistle)
                embed.set_author(name=lang["AUTHOR_NAME"], icon_url="https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif")
                await channel.send(embed=embed)

            else:
                embed = self.utils.permission_error("administrator", self.lang)
                await channel.send(embed=embed)
        else:
            await self.help.help("setlanguage")


    @client.event
    async def setprefix(self):
        import os
        lang    = self.lang["SETPREFIX"]
        channel = self.message.channel

        if len(self.message.content.split()) > 1:
            if len(self.message.content.split()[1]) <= 2:
                if self.member_perms.admin:

                    file = "configs/guilds configs/" + str(self.message.guild.id)  + ".json"  
                    model = self.utils.guild_confgs_model()
                    model["prefix"] = self.message.content.split()[1]

                    try:
                        if os.path.exists(file):
                            f = self.utils.open_json(file)
                            f["prefix"] = self.message.content.split()[1]
                            self.utils.write_json(file, f)
                        else:
                            self.utils.write_json(file, model)

                        embed = discord.Embed(title=lang["EMBED_TITLE"], description=self.message.content.split()[1], color=self.colors.Thistle)
                        embed.set_author(name=lang["AUTHOR_NAME"], icon_url="https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif")
                        await channel.send(embed=embed)

                    except:
                        await channel.send("`an unexpected error occurred`")
                else:
                    embed = self.utils.permission_error("administrator", self.lang)
                    await channel.send(embed=embed)
            else:
                await self.help.help("setprefix")
        else:
            await self.help.help("setprefix")
            