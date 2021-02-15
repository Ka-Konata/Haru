import discord
import os

client = discord.Client()

class Utils:
    def __init__(self, token=None):
        self.TOKEN = token


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

        usu         = Utils()

        português   = usu.open_json("languages/português")
        english     = usu.open_json("languages/english.json")
        languages   = {"português":português, "english":english}

        try:
            lang    = languages[usu.open_json("languages/guild_languages")[guild_id]]

        except Exception as erro:
            guilds_langs           = usu.open_json("languages/guild_languages")
            guilds_langs[guild_id] = "português"
            usu.write_json("languages/guild_languages", guilds_langs)
            lang    = languages[usu.open_json("languages/guild_languages")[guild_id]]
        return lang