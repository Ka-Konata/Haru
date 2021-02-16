import discord
import asyncio

client = discord.Client()

class Cmd_help:
    def __init__(self):
        pass


    # Comando Help
    @client.event
    async def help(self, message, aliases, lang, colors, prefixo, request="Null"):
        lang    = lang["HELP"]
        channel = message.channel

        embed   = discord.Embed(title=lang["HELP_EMBED_TITLE"], description=lang["HELP_EMBED_DESCRIPTION"], color=colors.roxoclaro)
        embed.set_author(name=lang["HELP_EMBED_AUTHOR_NAME"], icon_url="https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/808100198899384352/abdd8567a2531e4749fa0d29320bfe97.png")
        embed.add_field(name=lang["HELP_EMBED_FIELD_NAME"], value=lang["HELP_EMBED_FIELD_VALUE"], inline=False)
        embed.add_field(name=lang["HELP_EMBED_CONFGS_NAME"], value=lang["HELP_EMBED_CONFGS_VALUE"], inline=False)
        embed.add_field(name=lang["HELP_EMBED_UTILITY_NAME"], value=lang["HELP_EMBED_UTILITY_VALUE"], inline=True)
        embed.add_field(name=lang["HELP_EMBED_GAMES_NAME"], value=lang["HELP_EMBED_GAMES_VALUE"], inline=True)

        user_msg = message.content

        if len(user_msg.split()) == 1 and request == "Null":
            await channel.send(embed=embed)

        elif len(user_msg.split()) == 2 or request != "Null":
            if request != "Null":
                cmd = request
            else: 
                cmd = user_msg.split()[1]

            # ---------- HELP ----------

            if cmd in aliases.help:
                print("help")

            # ---------- CONFIGURATION ----------

            elif cmd in aliases.setlanguage:
                langcf = lang["SETLANGUAGE"]
                embed_setlanguage = discord.Embed(title=langcf["TITLE"], description=langcf["DESCRIPTION"], color=colors.Thistle)
                embed_setlanguage.set_author(name=langcf["AUTHOR_NAME1"] + f" {prefixo}help " + langcf["AUTHOR_NAME2"], icon_url="https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif")
                embed_setlanguage.add_field(name=langcf["USE_NAME"], value=f"`{prefixo}setlanguage`", inline=True)
                ex_value = f"`{prefixo}setlanguage en` `{prefixo}setlanguage pt_BR`"
                embed_setlanguage.add_field(name=langcf["EXAMPLE_NAME"], value=ex_value, inline=True)
                embed_setlanguage.add_field(name=langcf["LANGUAGES_NAME"], value="en, pt_BR", inline=True)
                embed_setlanguage.add_field(name=langcf["ALIASES_NAME"], value=f"`{prefixo}changelanguage` `{prefixo}language` `{prefixo}mudaridioma` `{prefixo}idioma`", inline=True)
                await channel.send(embed=embed_setlanguage)

            elif cmd in aliases.setprefix:
                langsp = lang["SETPREFIX"]
                embed_setprefix = discord.Embed(title=langsp["TITLE"], description=langsp["DESCRIPTION"], color=colors.Thistle)
                embed_setprefix.set_author(name=langsp["AUTHOR_NAME1"] + f" {prefixo}help " + langsp["AUTHOR_NAME2"], icon_url="https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif")
                embed_setprefix.add_field(name=langsp["USE_NAME"], value=f"`{prefixo}setprefix`", inline=True)
                ex_value = f"`{prefixo}setprefix ?` `{prefixo}setprefix h!`"
                embed_setprefix.add_field(name=langsp["EXAMPLE_NAME"], value=ex_value, inline=True)
                embed_setprefix.add_field(name=langsp["LIMIT_SIZE_T"], value=langsp["LIMIT_SIZE_VAL"], inline=True)
                embed_setprefix.add_field(name=langsp["ALIASES_NAME"], value=f"`{prefixo}changeprefix` `{prefixo}prefix` `{prefixo}mudarprefixo` `{prefixo}prefixo`", inline=True)
                await channel.send(embed=embed_setprefix)


            # ---------- UTILITY ----------

            elif cmd in aliases.morse:
                langm = lang["MORSE"]
                embed_morse = discord.Embed(title=langm["TITLE"], description=langm["DESCRIPTION"], color=colors.Thistle)
                embed_morse.set_author(name=langm["AUTHOR_NAME1"] + f" {prefixo}help " + langm["AUTHOR_NAME2"], icon_url="https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif")
                embed_morse.add_field(name=langm["USE_NAME"], value=f"`{prefixo}morse`", inline=True)
                ex_value = f"`{prefixo}morse Holla` `{prefixo}morse " + langm["EX_VAL1"] + "`"
                embed_morse.add_field(name=langm["EXAMPLE_NAME"], value=ex_value, inline=True)
                embed_morse.add_field(name=langm["ALIASES_NAME"], value=f"`{prefixo}codigomorse` `{prefixo}cm` `{prefixo}m` ", inline=True)
                await channel.send(embed=embed_morse)

            # ---------- GAMES ----------
            
            # Help comando Coin Flip
            elif cmd in aliases.coinflip:
                langcf = lang["COINFLIP"]
                embed_coinflip = discord.Embed(title=langcf["TITLE"], description=langcf["DESCRIPTION"], color=colors.Thistle)
                embed_coinflip.set_author(name=langcf["AUTHOR_NAME1"] + f" {prefixo}help " + langcf["AUTHOR_NAME2"], icon_url="https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif")
                embed_coinflip.add_field(name=langcf["USE_NAME"], value=f"`{prefixo}coinflip`", inline=True)
                ex_value = f"`{prefixo}coinflip " + langcf["EX_VAL1"] + "`" + f" `{prefixo}coinflip " + langcf["EX_VAL2"] + "`"
                embed_coinflip.add_field(name=langcf["EXAMPLE_NAME"], value=ex_value, inline=True)
                embed_coinflip.add_field(name=langcf["ALIASES_NAME"], value=f"`{prefixo}cf` `{prefixo}flip`", inline=True)
                await channel.send(embed=embed_coinflip)

            else:
                await channel.send(embed=embed)

        else:
            await channel.send(embed=embed)

    