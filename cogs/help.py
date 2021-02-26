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

        embed.add_field(name=lang["HELP_EMBED_FIELD_NAME"],   value=lang["HELP_EMBED_FIELD_VALUE"], inline=False)
        embed.add_field(name=lang["HELP_EMBED_CONFGS_NAME"],  value=lang["HELP_EMBED_CONFGS_VALUE"], inline=False)
        embed.add_field(name=lang["HELP_EMBED_MOD_NAME"],  value=lang["HELP_EMBED_MOD_VALUE"],   inline=False)
        embed.add_field(name=lang["HELP_EMBED_UTILITY_NAME"], value=lang["HELP_EMBED_UTILITY_VALUE"], inline=True)
        embed.add_field(name=lang["HELP_EMBED_GAMES_NAME"],   value=lang["HELP_EMBED_GAMES_VALUE"], inline=True)
        embed.add_field(name=lang["HELP_EMBED_FUN_NAME"],     value=lang["HELP_EMBED_FUN_VALUE"], inline=True)

        user_msg = self.message.content

        if len(user_msg.split()) == 1 and request == "Null":
            await channel.send(embed=embed)

        elif len(user_msg.split()) == 2 or request != "Null":
            if request != "Null":
                cmd = request
            else: 
                cmd = user_msg.split()[1]

            # ---------- HELP ----------

            if cmd in self.aliases.help["help"]:
                print("help")


            # ---------- CONFIGURATION ----------

            elif cmd in self.aliases.configuration["setlanguage"]:
                lang     = lang["SETLANGUAGE"]
                ex_value = f"```{self.prefixo}setlanguage en\n{self.prefixo}setlanguage pt-br```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.configuration["setlanguage"], extra1=True)
                
                await channel.send(embed=embed)

            elif cmd in self.aliases.configuration["setprefix"]:
                lang     = lang["SETPREFIX"]
                ex_value = f"```{self.prefixo}setprefix ?\n{self.prefixo}setprefix h!```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.configuration["setprefix"], extra1=True, howToUse=True)

                await channel.send(embed=embed)

            elif cmd in self.aliases.configuration["nsfw"]:
                lang     = lang["NSFW"]
                ex_value = f"```{self.prefixo}nsfw enable\n{self.prefixo}nsfw on```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.configuration["nsfw"], extra1=True, howToUse=True)

                await channel.send(embed=embed)

            elif cmd in self.aliases.configuration["settings"]:
                lang     = lang["SETTINGS"]
                ex_value = f"```{self.prefixo}settings```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.configuration["settings"])

                await channel.send(embed=embed)

            elif cmd in self.aliases.configuration["lockcommand"]:
                lang     = lang["LOCKCOMMAND"]
                ex_value = f"```{self.prefixo}lockcommand addrole\n{self.prefixo}lockcommand permissions```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.onfiguration["lockcommand"], howToUse=True)

                await channel.send(embed=embed)

            elif cmd in self.aliases.configuration["unlockcommand"]:
                lang     = lang["UNLOCKCOMMAND"]
                ex_value = f"```{self.prefixo}unlockcommand addrole\n{self.prefixo}unlockcommand permissions```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.configuration["unlockcommand"], howToUse=True)

                await channel.send(embed=embed)

            elif cmd in self.aliases.configuration["lockmodule"]:
                lang     = lang["LOCKMODULE"]
                ex_value = f"```{self.prefixo}lockmodule utility\n{self.prefixo}lockmodule moderation```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.configuration["lockmodule"], extra1=True, howToUse=True)

                await channel.send(embed=embed)

            elif cmd in self.aliases.configuration["unlockmodule"]:
                lang     = lang["UNLOCKMODULE"]
                ex_value = f"```{self.prefixo}unlockmodule utility\n{self.prefixo}unlockmodule moderation```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.configuration["unlockmodule"], extra1=True, howToUse=True)

                await channel.send(embed=embed)

            elif cmd in self.aliases.configuration["lockedcommands"]:
                lang     = lang["LOCKEDCOMMANDS"]
                ex_value = f"```{self.prefixo}lockedcommands utility\n{self.prefixo}lockedcommands moderation```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.configuration["lockedcommands"], howToUse=True)

                await channel.send(embed=embed)



            # ---------- MODERATION----------

            elif cmd in self.aliases.moderation["addrole"]:
                lang     = lang["ADDROLE"]
                ex_value = f"```{self.prefixo}addrole @Haru#0001 808101728594821181 \n{self.prefixo}addrole 808100198899384352 808101728594821181```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.moderation["addrole"], howToUse=True)
                
                await channel.send(embed=embed)

            elif cmd in self.aliases.moderation["removerole"]:
                lang     = lang["REMOVEROLE"]
                ex_value = f"```{self.prefixo}removerole @Haru#0001 808101728594821181 \n{self.prefixo}removerole 808100198899384352 808101728594821181```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.moderation["removerole"], howToUse=True)
                
                await channel.send(embed=embed)

            elif cmd in self.aliases.moderation["permissions"]:
                lang     = lang["PERMISSIONS"]
                ex_value = f"```{self.prefixo}permissions @Haru#0001 \n{self.prefixo}permissions 808100198899384352```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.moderation["permissions"], howToUse=True)
                
                await channel.send(embed=embed)

            # ---------- UTILITY ----------

            elif cmd in self.aliases.utility["morse"]:
                lang     = lang["MORSE"]
                ex_value = f"```{self.prefixo}morse Holla \n{self.prefixo}morse " + lang["EX_VAL1"] + "```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.utility["morse"])
                
                await channel.send(embed=embed)

            elif cmd in self.aliases.utility["invite"]:
                lang     = lang["MORSE"]
                ex_value = f"```{self.prefixo}invite```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.utility["invite"])
                
                await channel.send(embed=embed)

            elif cmd in self.aliases.utility["flipmsg"]:
                lang     = lang["FLIPMSG"]
                ex_value = f"```{self.prefixo}flipmsg Kono Dio da!```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.utility["flipmsg"], howToUse=True)
                
                await channel.send(embed=embed)

            elif cmd in self.aliases.utility["avatar"]:
                lang     = lang["AVATAR"]
                ex_value = f"```{self.prefixo}avatar \n" + f"{self.prefixo}avatar @Haru#0001" + "```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.utility["avatar"])
                
                await channel.send(embed=embed)




            # ---------- GAMES ----------
            
            # Help comando Coin Flip
            elif cmd in self.aliases.games["coinflip"]:
                lang     = lang["COINFLIP"]
                ex_value = f"```{self.prefixo}coinflip " + lang["EX_VAL1"] + "\n" + f"{self.prefixo}coinflip " + lang["EX_VAL2"] + "```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.games["coinflip"])
                
                await channel.send(embed=embed)

            elif cmd in self.aliases.games["dice"]:
                lang     = lang["DICE"]
                ex_value = f"```{self.prefixo}dice " + "\n" + f"{self.prefixo}dice 9" + "```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.games["dice"])
                
                await channel.send(embed=embed)

            elif cmd in self.aliases.games["guess"]:
                lang     = lang["GUESS"]
                ex_value = f"```{self.prefixo}guess 7```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.games["guess"])
                
                await channel.send(embed=embed)

            elif cmd in self.aliases.games["jokempo"]:
                lang     = lang["JOKEMPO"]
                ex_value = f"```{self.prefixo}jokempo pedra \n{self.prefixo}jokempo ✋```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.games["jokempo"])
                
                await channel.send(embed=embed)


            # ---------- FUN ----------

            elif cmd in self.aliases.fun["say"]:
                lang     = lang["SAY"]
                ex_value = f"```{self.prefixo}say Keanu Reeves é um grande gostoso" + f"\n{self.prefixo}say meu nome não é Haru```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.fun["say"])

                await channel.send(embed=embed)

            elif cmd in self.aliases.fun["send"]:
                lang     = lang["SEND"]
                ex_value = f"```{self.prefixo}send " + lang["EX_VAL1"]+ f"\n{self.prefixo}send " + lang["EX_VAL2"]
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.fun["send"], howToUse=True)

                await channel.send(embed=embed)

            elif cmd in self.aliases.fun["ship"]:
                lang     = lang["SHIP"]
                ex_value = f"```{self.prefixo}ship @Haru#0001" + f"\n{self.prefixo}ship 808100198899384352" + f"\n{self.prefixo}ship @Haru#0001 @Takagi#9867```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.fun["ship"], howToUse=True)

                await channel.send(embed=embed)

            elif cmd in self.aliases.fun["kiss"]:
                lang     = lang["KISS"]
                ex_value = f"```{self.prefixo}kiss @Haru#0001" + f"\n{self.prefixo}kiss 808100198899384352```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.fun["kiss"], howToUse=True)

                await channel.send(embed=embed)

            elif cmd in self.aliases.fun["hug"]:
                lang     = lang["HUG"]
                ex_value = f"```{self.prefixo}hug @Haru#0001" + f"\n{self.prefixo}hug 808100198899384352```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.fun["hug"], howToUse=True)

                await channel.send(embed=embed)

            elif cmd in self.aliases.fun["pat"]:
                lang     = lang["PAT"]
                ex_value = f"```{self.prefixo}pat @Haru#0001" + f"\n{self.prefixo}pat 808100198899384352```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.fun["pat"], howToUse=True)

                await channel.send(embed=embed)

            elif cmd in self.aliases.fun["slap"]:
                lang     = lang["SLAP"]
                ex_value = f"```{self.prefixo}slap @Haru#0001" + f"\n{self.prefixo}slap 808100198899384352```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.fun["slap"], howToUse=True)

                await channel.send(embed=embed)

            elif cmd in self.aliases.fun["shoot"]:
                lang     = lang["SHOOT"]
                ex_value = f"```{self.prefixo}shoot @Haru#0001" + f"\n{self.prefixo}shoot 808100198899384352```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.fun["shoot"], howToUse=True)

                await channel.send(embed=embed)

            elif cmd in self.aliases.fun["dance"]:
                lang     = lang["DANCE"]
                ex_value = f"```{self.prefixo}dance @Haru#0001" + f"\n{self.prefixo}dance 808100198899384352```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.fun["dance"], howToUse=True)

                await channel.send(embed=embed)

            elif cmd in self.aliases.fun["mugistrong"]:
                lang     = lang["MUGISTRONG"]
                ex_value = f"```{self.prefixo}mugistrong```"
                embed = self.utils.embed_model(lang, self.prefixo, self.colors, ex_value, self.aliases.fun["mugistrong"])

                await channel.send(embed=embed)



            else:
                await channel.send(lang["HELP_COMMAND_NOT_FOUND"] + f" `{cmd}` " + lang["HELP_COMMAND_NOT_FOUND2"])

        else:
            await channel.send(embed=embed)



