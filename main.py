import discord
import asyncio
import random
from sys import exit
from utils.usual import Utils
from utils import morse, aliases
from scripts.bot_token import secret_token as token


# Importando os comandos
from cogs.help import Cmd_help
help = Cmd_help()
from cogs.utility import Cmd_utility
utility = Cmd_utility()

client  = discord.Client()
TOKEN   = token.get_token()  # Make your file with your token
prefixo = ";"
utils   = Utils(TOKEN)

# Cores color
from utils import colors

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
    channel = message.channel
    
    lang = utils.set_language(prefixo, str(message.guild.id))

    # Comando Help
    if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.help)):
        await help.help(message, aliases, lang, colors, prefixo)

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
            await channel.send(lang["MESSAGE_PERMISSION_ERROR"])


    # Comando coinflip
    if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.coinflip)):
        await utility.coinflip(message, prefixo, lang)


    # Comando Morse
    if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.morse)):
        await utility.morse(message, prefixo, lang, morse_códigos, colors)


    # Comando Lol (uso apenas para teste durante a criação do bot)
    if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.lol)):
        global msg_id, msg_user, guild
        msg_user = message.author
        guild = message.guild

        embed_msg = discord.Embed(title="Escolha seu Elo!", color=colors.roxo, description="- bronze = 🌰 \n" "- prata = 🥄  \n" "- ouro = 🏆 \n")

        bot_msg = await channel.send(embed=embed_msg)
        await bot_msg.add_reaction("🌰")
        await bot_msg.add_reaction("🥄")
        await bot_msg.add_reaction("🏆")
        
        msg_id = bot_msg.id


@client.event
async def on_reaction_add(reaction, user):
    msg  = reaction.message

    # Comando Lol (uso apenas para teste durante a criação do bot)
    if reaction.emoji == "🌰" and msg.id == msg_id and user == msg_user:
        role = discord.utils.get(guild.roles, name="Bronze")
        await discord.Member.add_roles(msg_user, role)

    if reaction.emoji == "🥄" and msg.id == msg_id and user == msg_user:
        role = discord.utils.get(guild.roles, name="Prata")
        await discord.Member.add_roles(msg_user, role)

    if reaction.emoji == "🏆" and msg.id == msg_id and user == msg_user:
        role = discord.utils.get(guild.roles, name="Ouro")
        await discord.Member.add_roles(msg_user, role)


client.run(TOKEN)