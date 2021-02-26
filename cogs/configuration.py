import discord
import asyncio

client = discord.Client()

class Cmd_configuration:
    def __init__(self, message, lang, colors, member_perms, bot_perms, utils, help, prefixo, aliases):
        self.message      = message
        self.lang         = lang
        self.colors       = colors
        self.member_perms = member_perms
        self.utils        = utils
        self.help         = help
        self.prefixo      = prefixo
        self.aliases      = aliases

    # Comando Set Language
    @client.event
    async def setlanguage(self):
        lang    = self.lang["SETLANGUAGE"]
        channel = self.message.channel
        guild   = self.message.guild
        langs   = ("en", "pt-br")

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


    @client.event
    async def nsfw(self):
        import os
        lang    = self.lang["NSFW"]
        configs = self.utils.get_guild_configs(self.message.guild)
        content = self.message.content.split()
        arq     = "configs/guilds configs/" + str(self.message.guild.id)

        if len(content) > 1:
            if content[1].lower() in "enable/on":

                if configs["nsfw"] == False:
                    configs["nsfw"] = True
                    self.utils.write_json(arq, configs)
                    await self.message.add_reaction("✅")
                else:
                    await self.message.reply(lang["ALREADY_ON"])

            elif content[1].lower() in "disable/off":
                if configs["nsfw"] == True:
                    configs["nsfw"] = False
                    self.utils.write_json(arq, configs)
                    await self.message.add_reaction("✅")

                else:
                    await self.message.reply(lang["ALREADY_OFF"])
            else:
                await self.help.help(request="nsfw")
        else:
            await self.help.help(request="nsfw")


    @client.event
    async def settings(self):
        lang    = self.lang["SETTINGS"]
        confgs  = self.utils.get_guild_configs(self.message.guild)
        
        if confgs["nsfw"]:
            nsfw = lang["NSFW-ON"]
        else:
            nsfw = lang["NSFW-OFF"]

        embed   = discord.Embed(title= lang["EMBED_TITILE"] + self.message.guild.name, description=lang["EMBED_DESC"] + f" `{self.prefixo}help module configuration`", color=self.colors.Thistle)
        embed.set_author(name=self.message.author, icon_url=self.message.author.avatar_url)

        embed.add_field(name=lang["EMBED_PREFIX_NAME"] , value=confgs["prefix"])
        embed.add_field(name=lang["EMBED_LANG_NAME"] , value=confgs["language"])
        embed.add_field(name=lang["EMBED_LOCKED_NAME"] , value=len(confgs["locked_commands"]))
        embed.add_field(name=lang["EMBED_NSFW_NAME"] , value=nsfw)

        await self.message.reply(embed=embed)


    @client.event
    async def lockcommand(self):
        lang    = self.lang["LOCKCOMMAND"]
        content = self.message.content.split()
        configs = self.utils.get_guild_configs(self.message.guild)

        if len(content) > 1:
            if content[1].lower() in self.aliases.all:
                if not content[1].lower() in configs["locked_commands"] and not content[1].lower() != self.aliases.unlockcommand:

                    configs["locked_commands"].append(content[1].lower())
                    arq = "configs/guilds configs/" + str(self.message.guild.id)
                    self.utils.write_json(arq, configs)
                    await self.message.add_reaction("✅")
                
                elif content[1].lower() != self.aliases.configuration["unlockcommand"]:
                    await self.message.reply(lang["CANT_LOCK_COMMAND"])

                else:
                    await self.message.reply(lang["ALREADY_LOCKED"])
            else:
                await self.message.reply(self.lang["CMD_NOT_FOUND_ERROR"] + f"´{content[1]}´" + self.lang["CMD_NOT_FOUND_ERROR_2"])
        else:
            await self.help.help(request="lockcommand")


    @client.event
    async def unlockcommand(self):
        lang    = self.lang["UNLOCKCOMMAND"]
        content = self.message.content.split()
        configs = self.utils.get_guild_configs(self.message.guild)

        if len(content) > 1:
            if content[1].lower() in self.aliases.all:
                if content[1].lower() in configs["locked_commands"]:

                    configs["locked_commands"].remove(content[1].lower())
                    arq = "configs/guilds configs/" + str(self.message.guild.id)
                    self.utils.write_json(arq, configs)
                    await self.message.add_reaction("✅")

                else:
                    await self.message.reply(lang["ALREADY_UNLOCKED"])
            else:
                await self.message.reply(self.lang["CMD_NOT_FOUND_ERROR"] + f"`{content[1]}`" + self.lang["CMD_NOT_FOUND_ERROR_2"])
        else:
            await self.help.help(request="unlockcommand")


    @client.event
    async def lockmodule(self):
        lang    = self.lang["LOCKMODULE"]
        content = self.message.content.split()

        if len(content) > 1:
            pass
        else:
            await self.help.help(request="lockmodule")


    @client.event
    async def unlockmodule(self):
        lang    = self.lang["UNLOCKMODULE"]
        content = self.message.content.split()

        if len(content) > 1:
            pass
        else:
            await self.help.help(request="unlockmodule")


    @client.event
    async def lockedcommands(self):
        lang    = self.lang["LOCKEDCOMMANDS"]
            