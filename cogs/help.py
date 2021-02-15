import discord
import asyncio

client = discord.Client()
roxoclaro = 0xbbabc5


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

class Cmd_help:
    def __init__(self):
        pass

    @client.event
    async def help(self, message, aliases):
        lang    = languages[utils.open_json("languages/guild_language")[str(message.guild.id)]]["HELP"]
        channel = message.channel

        embed   = discord.Embed(title=lang["HELP_EMBED_TITLE"], description=lang["HELP_EMBED_DESCRIPTION"], color=roxoclaro)
        embed.set_author(name=lang["HELP_EMBED_AUTHOR_NAME"], icon_url="https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/808100198899384352/abdd8567a2531e4749fa0d29320bfe97.png")
        embed.add_field(name=lang["HELP_EMBED_FIELD_NAME"], value=lang["HELP_EMBED_FIELD_VALUE"], inline=False)
        embed.add_field(name=lang["HELP_EMBED_UTILITY_NAME"], value=lang["HELP_EMBED_UTILITY_VALUE"], inline=True)

        user_msg = message.content
        if len(user_msg.split()) == 1:
            await channel.send(embed=embed)

        elif len(user_msg.split()) == 2:
            cmd = user_msg.split()[1]
            if cmd in aliases.test:
                embed_test = discord.Embed(title="")

            elif cmd in aliases.stoprunning:
                print("stoprunning")

            elif cmd in aliases.help:
                print("help")

            elif cmd in aliases.coinflip:
                embed=discord.Embed(title="Comando coinflip", description="Deixe que a Haru joque uma moeda e tente adivinhar qual lado dela cairá virado para cima, cara ou coroa.")
embed.set_author(name="USE `h!help`  PARA VER TODOS OS COMANDOS.", icon_url="https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif")
embed.add_field(name="undefined", value="undefined", inline=False)
await ctx.send(embed=embed)

            elif cmd in aliases.morse:
                print("morse")

            else:
                await channel.send(embed=embed)

        else:
            await channel.send(embed=embed)

    