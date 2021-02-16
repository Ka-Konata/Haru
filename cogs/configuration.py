import discord
import asyncio

client = discord.Client()

class Cmd_Configuration:
    def __init__(self):
        pass

    # Comando Set Language
    @client.event
    async def setlanguage(self, message, _lang, colors, member_perms, utils, _help, aliases, prefixo):
        lang    = _lang["SETLANGUAGE"]
        channel = message.channel
        guild   = message.guild
        langs   = ("en", "pt_BR")

        if len(message.content.split()) > 1 and message.content.split()[1] in langs:

            if member_perms.admin:
                content = utils.open_json("languages/guild_languages.json")
                content[str(guild.id)] = message.content.split()[1]

                utils.write_json("languages/guild_languages.json", content)
                lang  = utils.set_language(prefixo, str(message.guild.id))["SETLANGUAGE"]

                embed = discord.Embed(title=message.content.split()[1])
                embed.set_author(name=lang["AUTHOR_NAME"], icon_url="https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif")
                await channel.send(embed=embed)

            else:
                embed = utils.permission_error("administrator", _lang)
                await channel.send(embed=embed)
        else:
            await _help.help(message, aliases, _lang, colors, prefixo, request="setlanguage")


    @client.event
    async def setprefix(self, message, lang, member_perms, colors, utils, prefixo):
        lang    = lang["PREFIX"]
        channel = message.channel

        if message.content.split() > 1:
            if len(message.content.split()[1]) <= 3:
                if member_perms.admin:

                    file = "configs/guilds configs/" + str(message.guild.id) + ".json"
                    model = utils.guild_confgs_model()
                    model["prefix"] = message.content.split()[1]

                    try:
                        f = utils.open_json(file)
                    except FileNotFoundError:
                        utils.write_json(file, model)

                else:
                    pass
            else:
                pass
        else:
            pass