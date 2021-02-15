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
prefixo = "h!"
utils   = Utils(TOKEN)

# languages
português = utils.open_json("languages/português")
english = utils.open_json("languages/english.json")
languages = {"português":português, "english":english}
lang = None



# Cores color
roxo     = 0x8E44AD
ciano    = 0x00FA9A

guild    = None
msg_id   = None
msg_user = None

morse_códigos = morse.get_morse()

@client.event
async def on_ready():
    channel = client.get_channel(788785603105259574)
    embed_msg = discord.Embed(title="BOT ONLINE - HELLO WORLD", color=ciano, description=f"**Bot UserName:**  {client.user.name} \n**Bot UserID:**  {client.user.id} \n**Channel:**  {channel.mention}")
    await channel.send(embed=embed_msg)
    print("BOT ONLINE - HELLO WORLD")
    print(client.user.name)
    print(client.user.id)
    print("-------------------------")


@client.event
async def on_message(message):
    channel = message.channel
    lang    = languages[utils.open_json("languages/guild_language")[str(message.guild.id)]]

    # Comando Help
    if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.help)):
        await help.help(message, aliases)

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
        await utility.coinflip(message, prefixo)


    # Comando Morse
    if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.morse)):
        if len(message.content.split()) < 2:
            await channel.send(lang["MORSE_MISSING_ERROR"] + f"\nexample: `{prefixo}morse Oi linda`")
        else:
            description = "**"
            frase = message.content.lower().split()[1:]

            for n, word in enumerate(frase):
                breakl = False
                word = list(word)
                for n2, letter in enumerate(word):

                    try:
                        description = description + morse_códigos[letter] + " "
                    except KeyError:
                        await channel.send("MORSE_UNKNOWN_CHARACTER_ERROR")
                        breakl = True
                        break

                    if n2 == len(word) - 1 and n < len(frase) - 1:
                        description = description + "/ "

                if breakl:
                    break
                elif n == len(frase) - 1:
                    description = description + "**"
                    embed_msg = discord.Embed(title=lang["MORSE_TRANSLATED_TITLE"], color=roxo, description=description)
                    await channel.send(embed=embed_msg)


    # Comando Lol (uso apenas para teste durante a criação do bot)
    if message.content.lower().startswith(utils.ins_prefix(prefixo, aliases.lol)):
        global msg_id, msg_user, guild
        msg_user = message.author
        guild = message.guild

        embed_msg = discord.Embed(title="Escolha seu Elo!", color=roxo, description="- bronze = 🌰 \n" "- prata = 🥄  \n" "- ouro = 🏆 \n")

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