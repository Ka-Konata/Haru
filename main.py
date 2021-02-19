import discord
import asyncio
import random
from sys import exit
from utils.usual import Utils
from utils import morse
from scripts import aliases, requeriments
from scripts.bot_token import secret_token as token

morse_códigos = morse.get_morse()
icon_url = "https://cdn.discordapp.com/avatars/502687173099913216/a_a1113f8f92b108969aad7d6925adb774.gif"


intents = discord.Intents.default()
intents.members = True

client  = discord.Client(intents=intents)
TOKEN   = token.get_token()  # Make your file with your token
prefixo = ";"
utils   = Utils(icon_url)

# Cores color
from scripts import colors

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
    if message.author.bot == False:
        member_perms = utils.get_permissions(message.author, requeriments)
        prefixo = utils.get_prefix(message.guild.id)
        channel = message.channel
        mentions = message.mentions
        
        lang = utils.set_language(prefixo, str(message.guild.id))

        # Importanto os comandos
        from cogs.help import Cmd_help
        help = Cmd_help(message, aliases, lang, colors, prefixo, utils)
        from cogs.configuration import Cmd_configuration
        confgs = Cmd_configuration(message, lang, colors, member_perms, utils, help, prefixo)
        from cogs.utility import Cmd_utility
        utility = Cmd_utility(message, aliases, prefixo, lang, colors)
        from cogs.games import Cmd_games
        games = Cmd_games(message, aliases, prefixo, lang, colors)
        from cogs.fun import Cmd_fun 
        fun = Cmd_fun(message, client, aliases, lang, colors, prefixo, help, mentions)


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

        # Comando Send
        if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.send)):
            await fun.send()


client.run(TOKEN)