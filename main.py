import discord
import asyncio
import random
from sys import exit
from utils.usual import Utils
from utils import morse
from scripts import aliases, requeriments
from scripts.bot_token import secret_token as token


client  = discord.Client()
TOKEN   = token.get_token()  # Make your file with your token
prefixo = ";"
utils   = Utils(TOKEN)

# Cores color
from scripts import colors

guild    = None
msg_id   = None
msg_user = None

morse_códigos = morse.get_morse()

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
    member_perms = utils.get_permissions(message.author, requeriments)
    prefixo = utils.get_prefix(message.guild.id)
    channel = message.channel
    
    lang = utils.set_language(prefixo, str(message.guild.id))

    # Importanto os comandos
    from cogs.help import Cmd_help
    help = Cmd_help(message, aliases, lang, colors, prefixo)
    from cogs.configuration import Cmd_configuration
    confgs = Cmd_configuration(message, lang, colors, member_perms, utils, help, prefixo)
    from cogs.utility import Cmd_utility
    utility = Cmd_utility(message, aliases, prefixo, lang, colors)
    from cogs.games import Cmd_games
    games = Cmd_games(message, aliases, prefixo, lang, colors)
    from cogs.fun import Cmd_fun
    fun = Cmd_fun(message, aliases, lang, colors, prefixo, help)


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
    if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.help)):
        await help.help()

    # ---------- MODERATION----------


    # ---------- CONFIGURATION ----------

    # Comando Set Language
    if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.setlanguage)):
        await confgs.setlanguage()

    # Comando Set Prefix
    if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.setprefix)):
        await confgs.setprefix()


    # ---------- UTILITY ----------
    
    # Comando Morse
    if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.morse)):
        await utility.morse(morse_códigos)

    # ---------- GAMES ----------

    # Comando coinflip
    if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.coinflip)):
        await games.coinflip()

    # ---------- FUN ----------

    # Comando Say
    if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.say)):
        await fun.say()


client.run(TOKEN)