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

class Cmd_help:
    def __init__(self):
        pass

    @client.event
    async def help(self, message, aliases, lang, colors, prefixo):
        lang    = lang["HELP"]
        channel = message.channel

        embed   = discord.Embed(title=lang["HELP_EMBED_TITLE"], description=lang["HELP_EMBED_DESCRIPTION"], color=colors.roxoclaro)
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
            
            # Help comando Coin Flip
            elif cmd in aliases.coinflip:
                langcf = lang["COINFLIP"]
                embed_coinflip = discord.Embed(title=langcf["TITLE"], description=langcf["DESCRIPTION"], color=colors.Thistle)
                embed_coinflip.set_author(name=langcf["AUTHOR_NAME1"] + f" {prefixo}help " + langcf["AUTHOR_NAME2"], icon_url="https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif")
                embed_coinflip.add_field(name=langcf["USE_NAME"], value=f"`{prefixo}coinflip`", inline=True)
                ex_value = f"`{prefixo}coinflip " + langcf["EX_VAL1"] + "`" + f" `{prefixo}coinflip " + langcf["EX_VAL2"] + "`"
                embed_coinflip.add_field(name=langcf["EXAMPLE_NAME"], value=ex_value, inline=True)
                embed_coinflip.add_field(name=langcf["ALIASES_NAME"], value=f"`{prefixo}coinflip` `{prefixo}cf` `{prefixo}flip`", inline=True)
                await channel.send(embed=embed_coinflip)

            elif cmd in aliases.morse:
                langm = lang["MORSE"]
                embed_morse = discord.Embed(title=langm["TITLE"], description=langm["DESCRIPTION"], color=colors.Thistle)
                embed_morse.set_author(name=langm["AUTHOR_NAME1"] + f" {prefixo}help " + langm["AUTHOR_NAME2"], icon_url="https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif")
                embed_morse.add_field(name=langm["USE_NAME"], value=f"`{prefixo}morse`", inline=True)
                ex_value = f"`{prefixo}morse Holla` `{prefixo}morse " + langm["EX_VAL1"] + "`"
                embed_morse.add_field(name=langm["EXAMPLE_NAME"], value=ex_value, inline=True)
                embed_morse.add_field(name=langm["ALIASES_NAME"], value=f"`{prefixo}morse` `{prefixo}codigomorse` `{prefixo}cm` `{prefixo}m` ", inline=True)
                await channel.send(embed=embed_morse)

            else:
                await channel.send(embed=embed)

        else:
            await channel.send(embed=embed)

    