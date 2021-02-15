import discord
import asyncio

client = discord.Client()


class Utils:
    def __init__(self, token=None):
        self.TOKEN = token

    def write_json(self, file, description, encoding="utf-8"):
        import json
        if not ".json" in file:
            file += ".json"
        with open(file, "w", encoding=encoding) as json_file:
           json.dump(description, json_file, indent=4)

    def open_json(self, file, encoding="utf-8"):
        import json
        if not ".json" in file:
            file += ".json"
        with open(file, "r", encoding=encoding) as json_file:
            content = json.load(json_file)
        return content

utils = Utils()

# Languages
português = utils.open_json("languages/português")
english = utils.open_json("languages/english.json")
languages = {"português":português, "english":english}
lang = None

class Cmd_utility:
    def __init__(self):
        pass

    # Comando Coin Flip
    @client.event
    async def coinflip(self, message, prefixo):
        import random
        lang    = languages[utils.open_json("languages/guild_language")[str(message.guild.id)]]["HELP"]
        channel = message.channel

        num = random.randint(0, 1)
        coin = ["cara", "coroa"]
        if not "cara" in message.content.lower() and not "coroa" in message.content.lower():
            await channel.send(lang["COINFLIP_MISSING_ERROR"] + f"\nexample: `{prefixo}coinflip cara`")
        else:
            result = lang["WIN"] if coin[num] in message.content.lower().split()[1] else lang["LOSE"]
            if num == 0:
                await channel.send(lang["COINFLIP_RESULT_CARA"] + f" **{result}**!")
            elif num == 1:
                await channel.send(lang["COINFLIP_RESULT_COROA"] + f" **{result}**!")

    # Comando Morse
    @client.event
    async def morse(self, message, prefixo):
        import random
        lang    = languages[utils.open_json("languages/guild_language")[str(message.guild.id)]]["HELP"]
        channel = message.channel