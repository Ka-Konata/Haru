import discord
import asyncio

client = discord.Client()

class Cmd_mod:
    def __init__(self, message, aliases, prefixo, lang, client, colors, help, mentions, member_perms, bot_perms, utils, icon_url):
        self.message      = message
        self.aliases      = aliases
        self.prefixo      = prefixo
        self.lang         = lang
        self.client       = client
        self.colors       = colors
        self._help        = help
        self.mentions     = mentions 
        self.member_perms = member_perms
        self.bot_perms    = bot_perms
        self.utils        = utils
        self.icon_url     = icon_url


    @client.event
    async def addrole(self):
        #lang    = self.lang["ADDROLE"]
        content = self.message.content.split()

        if self.bot_perms.manage_roles:
            if self.member_perms.mod:
                if len(content) > 2:
                    user = await self.utils.get_member(content[1], self.mentions, self.message, self.lang)
                    if user != None:
                        try:
                            role = self.message.guild.get_role(int(content[2]))
                        except ValueError:
                            role = None

                        if role != None:
                            try:
                                await user.add_roles(role)
                                await self.message.add_reaction("✅")
                            except discord.errors.Forbidden:
                                embed = discord.Embed(title=self.lang["ROLE_HIGHER_ERROR_TITLE"])
                                embed.set_author(name=self.lang["ROLE_HIGHER_ERROR_AUTHOR_NAME"], icon_url=self.icon_url)
                                await self.message.reply(embed=embed)
                        else:
                            await self.message.reply(self.lang["ROLE_NOT_FOUND_ERROR"] + "`" + content[2] + "`")
                else:
                    await self._help.help(request="addrole")
            else:
                embed = self.utils.permission_error("moderador", self.lang)
                await self.message.reply(embed=embed)
        else:
            embed = self.utils.bot_permission_error("manege_roles", self.lang)
            await self.message.reply(embed=embed)


    @client.event
    async def removerole(self):
        #lang    = self.lang["ADDROLE"]
        content = self.message.content.split()

        if self.bot_perms.manage_roles:
            if self.member_perms.mod:
                if len(content) > 2:
                    user = await self.utils.get_member(content[1], self.mentions, self.message, self.lang)
                    if user != None:
                        try:
                            role = self.message.guild.get_role(int(content[2]))
                        except ValueError:
                            role = None

                        if role != None:
                            try:
                                await user.remove_roles(role)
                                await self.message.add_reaction("✅")
                            except discord.errors.Forbidden:
                                embed = discord.Embed(title=self.lang["ROLE_HIGHER_ERROR_TITLE"])
                                embed.set_author(name=self.lang["ROLE_HIGHER_ERROR_AUTHOR_NAME"], icon_url=self.icon_url)
                                await self.message.reply(embed=embed)
                        else:
                            await self.message.reply(self.lang["ROLE_NOT_FOUND_ERROR"] + "`" + content[2] + "`")
                else:
                    await self._help.help(request="addrole")
            else:
                embed = self.utils.permission_error("moderador", self.lang)
                await self.message.reply(embed=embed)
        else:
            embed = self.utils.bot_permission_error("manege_roles", self.lang)
            await self.message.reply(embed=embed)
