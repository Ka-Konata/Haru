import discord
import asyncio

client = discord.Client()

class Cmd_games:
    def __init__(self, message, aliases, prefixo, lang, colors, help):
        self.message = message
        self.aliases = aliases
        self.prefixo = prefixo
        self.lang    = lang
        self.colors  = colors
        self._help   = help

    
    # Comando Coin Flip
    @client.event
    async def coinflip(self):
        from random import randint
        lang    = self.lang["COINFLIP"]
        channel = self.message.channel

        num     = randint(0, 1)
        coin    = ["cara", "coroa"]

        if not "cara" in self.message.content.lower() and not "coroa" in self.message.content.lower():
            await channel.send(lang["COINFLIP_MISSING_ERROR"] + f"\nexample: `{self.prefixo}coinflip cara`")
        else:
            result = lang["WIN"] if coin[num] in self.message.content.lower().split()[1] else lang["LOSE"]

            if num   == 0:
                await channel.send(lang["COINFLIP_RESULT_CARA"] + f" **{result}**!")
            elif num == 1:
                await channel.send(lang["COINFLIP_RESULT_COROA"] + f" **{result}**!")

    
    # Comando Dice
    @client.event
    async def dice(self):
        from random import randint
        lang    = self.lang["DICE"]
        content = self.message.content.split()
        lados   = 6

        if len(content) > 1:
            try:
                lados = int(content[1])
            except ValueError:
                pass 
        else:
            lados = 6

        choice = randint(0, lados)
        await self.message.reply("🎲| " + self.message.author.mention + lang["ROLLING"] + "**" + str(lados) + "**" + lang["RESULT"] + "**" + str(choice) + "!**")


    # Comando guess
    @client.event
    async def guess(self):
        from random import randint
        lang    = self.lang["GUESS"]
        content = self.message.content.split()

        if len(content) > 1:
            if content[1].isnumeric():
                num = randint(0, 10)
                if int(content[1]) == num:
                    await self.message.reply(lang["MIND"] + str(num) + lang["GUESSED"] + content[1] + lang["WIN"])
                else:
                    await self.message.reply(lang["MIND"] + str(num) + lang["GUESSED"] + content[1] + lang["LOSE"])
            else:
                await self._help.help(request="guess")
        else:
            await self._help.help(request="guess")


    # Comando jokempo
    @client.event
    async def jokempo(self):
        from random import choice 
        lang     = self.lang["JOKEMPO"]
        content  = self.message.content.split()
        emojis   = ["✊", "✋", "✌️"]

        if len(content) > 1:
            if content[1] in lang["CHOICES"] or content[1] in lang["CHOICES_EMOJI"]:
                choice = choice(emojis)
                j      = content[1]

                if j in lang["CHOICES_EMOJI"]:
                    j = lang[j]

                if j == lang[choice]:
                    result = lang["BREAK_EVEN"]
                elif lang[choice] == lang["CH"][j]:
                    result = lang["WIN"]
                else:
                    result = lang["LOSE"]

                await self.message.reply(lang["I_CHOSED"] + lang[choice] + " " + choice + result)

            else:
                await self.message.reply("Escolha entre um desses para jogar: \n**" + lang["CHOICES"] + "** " + lang["CHOICES_EMOJI"])
        else:
            await self._help.help(request="jokempo")
