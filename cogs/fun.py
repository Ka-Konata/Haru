import discord
import asyncio

client = discord.Client()

class Cmd_fun:
    def __init__(self):
        pass


    # Comando <name>
    @client.event
    async def name(self, message, aliases, lang, colors, prefixo, request="Null"):
        pass