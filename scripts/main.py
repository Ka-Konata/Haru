import discord
import asyncio
import random
from sys import exit
import bot_token.secret_token as token
import morse


client  = discord.Client()
TOKEN   = token.get_token()  # Make your file with your token
prefixo = "?"

guild    = None
color    = 0x8E44AD
msg_id   = None
msg_user = None

morse_códigos = morse.get_morse()

@client.event
async def on_ready():
    print("BOT ONLINE - HELLO WORLD")
    print(client.user.name)
    print(client.user.id)
    print("-------------------------")


@client.event
async def on_message(message):
    channel = message.channel

    # Comando Test, para testar se o bot está online
    if message.content.lower().startswith(prefixo + "test"):
        await channel.send("Hello world, I'm alive.")

    # Comando Stop Running, restrição: bot onwer
    if message.content.lower().startswith(prefixo + "stoprunning"):
        if message.author.id == 502687173099913216:
            await channel.send("Encerrando o script...")
            print("Encerrando o script...")
            exit()
        else:
            await channel.send("Você não tem permissão para executar esse comando")

    # Comando coinflip
    if message.content.lower().startswith(f"{prefixo}coinflip"):
        num = random.randint(0, 1)
        coin = ["cara", "coroa"]
        if not "cara" in message.content.lower() and not "coroa" in message.content.lower():
            await channel.send(f"Não se esqueça de colocar **cara** ou **coroa** ao lado do comando! \nexemplo: `{prefixo}coinflip cara`")
        else:
            result = "venceu" if coin[num] in message.content.lower().split()[1] else "perdeu"
            if num == 0:
                await channel.send(f"**FLIP!** | deu cara, você **{result}**!")
            elif num == 1:
                await channel.send(f"**FLIP!** | deu coroa, você **{result}**!")

    # Comando Morse
    if message.content.lower().startswith(f"{prefixo}morse"):
        if len(message.content.split()) < 2:
            await channel.send(f"Escreva a frase ou texto a ser traduzida ao lado do comando \nexemplo: `{prefixo}morse Oi linda`")
        else:
            description = ""
            frase = message.content.lower().split()[1:]

            for n, word in enumerate(frase):
                breakl = False
                word = list(word)
                for n2, letter in enumerate(word):

                    try:
                        description = description + morse_códigos[letter] + " "
                    except KeyError:
                        await channel.send("A mensagem a ser traduzida contém caracteres que eu não sou capaz de entender.")
                        breakl = True
                        break

                    if n2 == len(word) - 1 and n < len(frase) - 1:
                        description = description + "/ "

                if breakl:
                    break
                elif n == len(frase) - 1:
                    embed_msg = discord.Embed(title=f"Convertido para código morse:", color=color, description=description)
                    await channel.send(embed=embed_msg)

    # Comando Lol (uso apenas para teste durante a criação do bot)
    if message.content.lower().startswith(prefixo + "lol"):
        global msg_id, msg_user, guild
        msg_user = message.author
        guild = message.guild

        embed_msg = discord.Embed(title = "Escolha seu Elo!", color = color, description = "- bronze = 🌰 \n" "- prata = 🥄  \n" "- ouro = 🏆 \n")

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