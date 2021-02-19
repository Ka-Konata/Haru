import discord
import os
from discord.ext.commands import has_permissions, MissingPermissions

client = discord.Client()

class Utils:
    def __init__(self, icon_url, token=None):
        self.TOKEN    = token
        self.icon_url = icon_url


    def write_json(self, file, description, encoding="utf-8"):
        """
        create and/or write in a .json file
        file:          file name
        description:   the value to be saved in the file
        encoding:      encoding wich will be used
        """
        import json

        if not ".json" in file:
            file += ".json"

        with open(file, "w", encoding=encoding) as json_file2:
            json.dump(description, json_file2, indent=4)


    def open_json(self, file, encoding="utf-8"):
        """
        open a .json file
        file:     file name 
        encoding: encoding wich will be used
        return returns a variable with the contents of the file
        """
        import json

        if not ".json" in file:
            file += ".json"

        content = {}
        if os.path.exists(file): 
            with open(file, "r", encoding=encoding) as f:
                content = json.load(f)
        return content

    def ins_prefix(self, prefix, command):
        """
        inserts the prefix in each alias of a command
        prefix:     inserts the prefix in each alias of a command
        command:    command alias list
        return alias list with the prefix
        """
        aliases = []
        for aliase in command:
            aliase = prefix + aliase
            aliases.append(aliase)
        aliases = tuple(aliases)
        return aliases

    
    def set_language(self, prefix, guild_id):  #message
        """
        search the defined language for the guild
        prefix:      guild prefix
        guild:       guild id of the message
        """

        usu          = Utils(self.icon_url)

        português_BR = usu.open_json("languages/pt_BR")
        english      = usu.open_json("languages/en.json")
        languages    = {"pt_BR":português_BR, "en":english}

        try:
            lang     = languages[usu.open_json("languages/guild_languages")[guild_id]]

        except:
            guilds_langs           = usu.open_json("languages/guild_languages")
            guilds_langs[guild_id] = "pt_BR"
            usu.write_json("languages/guild_languages", guilds_langs)
            lang     = languages[usu.open_json("languages/guild_languages")[guild_id]]
        return lang

    
    def get_permissions(self, member, requeriments):
        """"""
        perms = member.guild_permissions
        level = requeriments.Requeriments()
        
        if perms.administrator:
            level.admin  = True
            level.mod    = True
            level.member = True

        elif perms.ban_members:
            level.admin  = False
            level.mod    = True
            level.member = True

        elif perms.send_messages:
            level.admin  = False
            level.mod    = False
            level.member = True

        return level
    

    def permission_error(self, permission, lang):
        embed = discord.Embed(title=lang["PERMISSION_ERROR_TITLE"])
        embed.set_author(name=lang["PERMISSION_ERROR_AUTHOR_NAME"], icon_url=self.icon_url)
        embed.add_field(name=lang["PERMISSION_ERROR_FIELD_NAME"], value=permission, inline=True)

        return embed

    def guild_confgs_model(self):
        model = {
            "prefix":"h!"
        }

        return model

    def get_prefix(self, guild_id):
        from os import path

        usu  = Utils(self.icon_url)

        file = "configs/guilds configs/" + str(guild_id)  + ".json"

        if not path.exists(file):
            model = usu.guild_confgs_model()
            model["prefix"] = "h!"
            usu.write_json(file, model)
            return "h!"
 
        else:
            f = usu.open_json(file)
            prefix = f["prefix"]
            return prefix


    def embed_model(self, lang, prefixo, colors, ex_value, aliases, extra1=False, extra2=False, howToUse=False):
        embed = discord.Embed(title=lang["TITLE"], description=lang["DESCRIPTION"], color=colors.Thistle)
        embed.set_author(name=lang["AUTHOR_NAME1"] + f" {prefixo}help " + lang["AUTHOR_NAME2"], icon_url=self.icon_url)

        if howToUse:
            embed.add_field(name=lang["USE_NAME"], value="```" + prefixo + lang["USE_VALUE"] + "```", inline=True)
        if extra1:
            embed.add_field(name=lang["EXTRA1_NAME"], value=lang["EXTRA1_VALUE"], inline=True)
        if extra2:
            embed.add_field(name=lang["EXTRA2_NAME"], value=lang["EXTRA2_VALUE"], inline=True)

        embed.add_field(name=lang["EXAMPLE_NAME"], value=ex_value, inline=True)

        _aliases = "```"
        for n, alias in enumerate(aliases):
            if n + 1 == len(aliases):
                _aliases = _aliases + alias + "```"
                break
            _aliases = _aliases + alias + ", " 

        embed.add_field(name=lang["ALIASES_NAME"], value=_aliases, inline=True)

        return embed
