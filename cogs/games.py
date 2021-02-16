import discord
import asyncio

client = discord.Client()

class Cmd_Games:
    def __init__(self):
        pass

    
    # Comando Coin Flip
    @client.event
    async def coinflip(self, message, prefixo, lang):
        import random
        lang = lang["COINFLIP"]
        channel = message.channel

        num = random.randint(0, 1)
        coin = ["cara", "coroa"]
        if not "cara" in message.content.lower() and not "coroa" in message.content.lower():
            await channel.send(lang["COINFLIP_MISSING_ERROR"] + f"\nexample: `{prefixo}coinflip cara`")
        else:
            result = lang["WIN"] if coin[num] in message.content.lower().split()[1] else lang["LOSE"]
            if num == 0:
                await channel.send(lang["COINFLIP_RESULT_CARA"] + f" **{result}**!")
            elif num == 1:
                await channel.send(lang["COINFLIP_RESULT_COROA"] + f" **{result}**!")