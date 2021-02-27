import discord
import asyncio
import random
import requests
from scripts           import ship
from sys               import exit
from utils.usual       import Utils
from utils             import morse
from scripts           import aliases, requeriments, permissions
from scripts.format    import toPNG
from scripts.bot_token import secret_token as token

morse_códigos = morse.get_morse()
icon_url = "https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif"


intents = discord.Intents.default()
intents.members = True

client  = discord.Client(intents=intents)
TOKEN   = token.get_token()  # Make your file with your token
prefixo = "h!"
utils   = Utils(icon_url, client)
guilds_security_coding = ["788518735752724480"]  # "796451246864203816" "803997027733471242"

# Cores e Gifs
from scripts import colors
from scripts import gifs

guild    = None
msg_id   = None
msg_user = None


@client.event
async def on_ready():
    channel = client.get_channel(788785603105259574)
    embed_msg = discord.Embed(title="BOT ONLINE - HELLO WORLD", color=colors.ciano, description=f"**Bot UserName:**  {client.user.name} \n**Bot UserID:**  {client.user.id} \n**Channel:**  {channel.mention}")
    await channel.send(embed=embed_msg)
    print("BOT ONLINE - HELLO WORLD")
    print(client.user.name)
    print(client.user.id)
    print("-------------------------")


@client.event
async def on_message(message):
    global icon_url, guilds_security_coding

    prefixo      = utils.get_prefix(message.guild.id)
    channel      = message.channel
    mentions     = message.mentions
        
    lang   = utils.set_language(prefixo, message.guild)
    confgs = utils.get_guild_configs(message.guild)

    # Security Guild Coding edit
    if message.author.id == 502687173099913216:

        if message.content.lower().startswith(f"h!addguildtocodingtests"):
            guilds_security_coding.append(str(message.guild.id))
            await message.add_reaction("✅")
            print(guilds_security_coding)

        elif message.content.lower().startswith(f"h!removeguildfromcodingtests") and str(message.guild.id) in guilds_security_coding:
            n = guilds_security_coding.index(str(message.guild.id))
            guilds_security_coding.remove(n)
            await message.add_reaction("✅")
            print(guilds_security_coding)

    modules = [aliases.help, aliases.configuration, aliases.utility, aliases.games, aliases.fun] 
    locked  = []
    for mod in modules:
        for cmd in mod:
            if cmd in (utils.ins_prefix(prefixo, confgs["locked_commands"])):
                locked.append(cmd)

    if message.author.bot == False and str(message.guild.id) in guilds_security_coding:
        if not message.content.split()[0].lower() in (utils.ins_prefix(prefixo, locked)):

            member_perms = utils.get_permissions(message.author, requeriments)
            bot_perms    = message.guild.get_member(808100198899384352).guild_permissions
            url = message.author.avatar_url
            if url != None:
                icon_url = url

            # Importanto os comandos
            from cogs.help          import Cmd_help
            from cogs.configuration import Cmd_configuration
            from cogs.moderation    import Cmd_mod
            from cogs.utility       import Cmd_utility
            from cogs.games         import Cmd_games
            from cogs.fun           import Cmd_fun 

            help    = Cmd_help(message, aliases, lang, colors, prefixo, utils)
            confgs  = Cmd_configuration(message, lang, colors, member_perms, bot_perms, utils, help, prefixo, aliases)
            mod     = Cmd_mod(message, aliases, prefixo, lang, client, colors, help, mentions, member_perms, bot_perms, utils, icon_url)
            utility = Cmd_utility(message, aliases, prefixo, lang, colors, help, client)
            games   = Cmd_games(message, aliases, prefixo, lang, colors, help)
            fun     = Cmd_fun(message, client, aliases, lang, colors, prefixo, help, utils, mentions)


            # Comando Test, para testar se o bot está online
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.test)):
                print(utils.ins_prefix(prefixo, aliases.test))
                await channel.send("Hello world, I'm alive.")


            # Comando Stop Running, restrição: bot onwer
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.stoprunning)):
                if message.author.id == 502687173099913216:
                    await channel.send(lang["FINAL_MESSAGE_EXECUTING"])
                    print("Encerrando o script...")
                    exit()
                else:
                    embed_error = utils.permission_error("bot owner", lang)
                    await channel.send(embed_error)


            # ---------- HELP ----------

            # Comando Help
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.help["help"])):
                await help.help()

            # ---------- CONFIGURATION ----------

            # Comando Set Language
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.configuration["setlanguage"])):
                await confgs.setlanguage()

            # Comando Set Prefix
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.configuration["setprefix"])):
                await confgs.setprefix()

            # Comando NSFW
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.configuration["nsfw"])):
                await confgs.nsfw()

            # Comando Settings
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.configuration["settings"])):
                await confgs.settings()

            # Comando Lock Command
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.configuration["lockcommand"])):
                await confgs.lockcommand()

            # Comando Unlock Command
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.configuration["unlockcommand"])):
                await confgs.unlockcommand()

            # Comando Lock Module
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.configuration["lockmodule"])):
                await confgs.lockmodule(modules)

            # Comando Unlock Module
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.configuration["unlockmodule"])):
                await confgs.unlockmodule()

            # Comando Locked Commands
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.configuration["lockedcommands"])):
                await confgs.lockedcommands()

            # ---------- MODERATION----------

            # Comando Add Role
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.moderation["addrole"])):
                await mod.addrole()

            # Comando Remove Role
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.moderation["removerole"])):
                await mod.removerole()

            # Comando Permissions
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.moderation["permissions"])):
                await mod.permissions(permissions)


            # ---------- UTILITY ----------
            
            # Comando Morse
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.utility["morse"])):
                await utility.morse(morse_códigos)

            # Comando Invite
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.utility["invite"])):
                await utility.invite()

            # Comando Flip MSG
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.utility["flipmsg"])):
                await utility.flipmsg()

            # Comando Avatar
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.utility["avatar"])):
                await utility.avatar()

            # ---------- GAMES ----------

            # Comando coinflip
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.games["coinflip"])):
                await games.coinflip()

            # Comando Dice
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.games["dice"])):
                await games.dice()

            # Comando Guess
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.games["guess"])):
                await games.guess()

            # Comando Jokempo
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.games["jokempo"])):
                await games.jokempo()

            # ---------- FUN ----------

            # Comando Say
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.fun["say"])):
                await fun.say()

            # Comando Send
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.fun["send"])):
                await fun.send()

            # Comando Ship
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.fun["ship"])):
                await fun.ship(ship, toPNG)

            # Comando Kiss
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.fun["kiss"])):
                await fun.kiss(gifs)

            # Comando Hug
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.fun["hug"])):
                await fun.hug(gifs)

            # Comando Pat
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.fun["pat"])):
                await fun.pat(gifs)

            # Comando Slap
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.fun["slap"])):
                await fun.slap(gifs)

            # Comando Shoot
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.fun["shoot"])):
                await fun.shoot(gifs)

            # Comando Dance
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.fun["dance"])):
                await fun.dance(gifs)

            # Comando Mugi Strong
            if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.fun["mugistrong"])):
                await fun.mugistrong(gifs)
        else:
            await message.reply(lang["COMMAND_LOCKED_ERROR"] + f"`{prefixo}unlockcommand [command]`")

    if message.author.id == 808100198899384352:
        try:
            if lang["KISS"]["MADE"] in message.embeds[0].description:
                await message.add_reaction("↪️")

            elif lang["HUG"]["MADE"] in message.embeds[0].description:
                await message.add_reaction("↪️")

            elif lang["PAT"]["MADE"] in message.embeds[0].description:
                await message.add_reaction("↪️")

            elif lang["SLAP"]["MADE"] in message.embeds[0].description:
                await message.add_reaction("↪️")

            elif lang["SHOOT"]["MADE"] in message.embeds[0].description:
                await message.add_reaction("↪️")

            elif lang["DANCE"]["MADE"] in message.embeds[0].description:
                await message.add_reaction("↪️")

        except:
            pass


@client.event
async def on_reaction_add(reaction, user):
    prefixo = utils.get_prefix(reaction.message.guild.id)
        
    lang = utils.set_language(prefixo, reaction.message.guild)

    if reaction.message.author.id == 808100198899384352:
        
        reference = reaction.message.reference.resolved

        # Importings the commands
        from cogs.help import Cmd_help
        from cogs.fun  import Cmd_fun
        help = Cmd_help(reference, aliases, lang, colors, prefixo, utils)
        fun  = Cmd_fun(reference, client, aliases, lang, colors, prefixo, help, utils, reference.mentions)

        same = False
        try:
            if user.id == reference.mentions[0].id and len(reference.mentions) < 2:
                same = True
        except IndexError:
            pass
        
        if prefixo in reference.content and (same or str(user.id) in reference.content.split()[1]) and reaction.emoji == "↪️":

            if lang["KISS"]["MADE"] in reaction.message.embeds[0].description:
                await fun.kiss(gifs, reply=True)

            elif lang["HUG"]["MADE"] in reaction.message.embeds[0].description:
                await fun.hug(gifs, reply=True)

            elif lang["PAT"]["MADE"] in reaction.message.embeds[0].description:
                await fun.pat(gifs, reply=True)

            elif lang["SLAP"]["MADE"] in reaction.message.embeds[0].description:
                await fun.slap(gifs, reply=True)

            elif lang["SHOOT"]["MADE"] in reaction.message.embeds[0].description:
                await fun.shoot(gifs, reply=True)

            elif lang["DANCE"]["MADE"] in reaction.message.embeds[0].description:
                await fun.dance(gifs, reply=True)


client.run(TOKEN)
