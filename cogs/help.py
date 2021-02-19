import discord
import asyncio

client = discord.Client()

class Cmd_help:
    def __init__(self, message, aliases, lang, colors, prefixo, utils):
        self.message = message
        self.aliases = aliases
        self.lang    = lang
        self.colors  = colors
        self.prefixo = prefixo
        self.utils   = utils


    # Comando Help
    @client.event
    async def help(self, request="Null"):
        lang    = self.lang["HELP"]
        channel = self.message.channel

        embed   = discord.Embed(title=lang["HELP_EMBED_TITLE"], description=lang["HELP_EMBED_DESCRIPTION"], color=self.colors.roxoclaro)
        embed.set_author(name=lang["HELP_EMBED_AUTHOR_NAME"], icon_url="https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/808100198899384352/abdd8567a2531e4749fa0d29320bfe97.png")
        embed.add_field(name=lang["HELP_EMBED_FIELD_NAME"], value=lang["HELP_EMBED_FIELD_VALUE"], inline=False)
        embed.add_field(name=lang["HELP_EMBED_CONFGS_NAME"], value=lang["HELP_EMBED_CONFGS_VALUE"], inline=False)
        embed.add_field(name=lang["HELP_EMBED_UTILITY_NAME"], value=lang["HELP_EMBED_UTILITY_VALUE"], inline=True)
        embed.add_field(name=lang["HELP_EMBED_GAMES_NAME"], value=lang["HELP_EMBED_GAMES_VALUE"], inline=True)
        embed.add_field(name=lang["HELP_EMBED_FUN_NAME"], value=lang["HELP_EMBED_FUN_VALUE"], inline=True)

        user_msg = self.message.content

        if len(user_msg.split()) == 1 and request == "Null":
            await channel.send(embed=embed)

        elif len(user_msg.split()) == 2 or request != "Null":
            if request != "Null":
                cmd = request
            else: 
                cmd = user_msg.split()[1]

            # ---------- HELP ----------

            if cmd in self.aliases.help:
                print("help")


            # ---------- CONFIGURATION ----------

            elif cmd in self.aliases.setlanguage:
                lang = lang["SETLANGUAGE"]
                ex_value = f"```{self.prefixo}setlanguage en\n{self.prefixo}setlanguage pt_BR```"
                embed_setlanguage = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.setlanguage, extra1=True)
                
                await channel.send(embed=embed_setlanguage)

            elif cmd in self.aliases.setprefix:
                lang = lang["SETPREFIX"]
                ex_value = f"```{self.prefixo}setprefix ?\n{self.prefixo}setprefix h!```"
                embed_setprefix = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.setprefix, extra1=True, howToUse=True)

                await channel.send(embed=embed_setprefix)


            # ---------- MODERATION----------

            # ---------- UTILITY ----------

            elif cmd in self.aliases.morse:
                lang = lang["MORSE"]
                ex_value = f"```{self.prefixo}morse Holla \n{self.prefixo}morse " + lang["EX_VAL1"] + "```"
                embed_morse = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.morse)
                
                await channel.send(embed=embed_morse)


            # ---------- GAMES ----------
            
            # Help comando Coin Flip
            elif cmd in self.aliases.coinflip:
                lang = lang["COINFLIP"]
                ex_value = f"```{self.prefixo}coinflip " + lang["EX_VAL1"] + "\n" + f"{self.prefixo}coinflip " + lang["EX_VAL2"] + "```"
                embed_coinflip = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.coinflip)
                
                await channel.send(embed=embed_coinflip)


            # ---------- FUN ----------

            elif cmd in self.aliases.say:
                lang = lang["SAY"]
                ex_value = f"```{self.prefixo}say Keanu Reeves é um grande gostoso" + f"\n{self.prefixo}say meu nome não é Haru```"
                embed_say = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.say)

                await channel.send(embed=embed_say)

            elif cmd in self.aliases.send:
                lang = lang["SEND"]
                ex_value = f"```{self.prefixo}send @Haru#0001 oi por quanto você vende o pack da mão?" + f"\n{self.prefixo}send @Haru#0001 me manda uma foto da parte de trás do seu cartão é pro meu TCC```"
                embed_send = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.send, howToUse=True)

                await channel.send(embed=embed_send)


            else:
                await channel.send(lang["HELP_COMMAND_NOT_FOUND"] + f" `{cmd}` " + lang["HELP_COMMAND_NOT_FOUND2"])

        else:
            await channel.send(embed=embed)



