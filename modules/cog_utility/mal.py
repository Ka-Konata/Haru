import discord, requests, typing, malclient
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors, mal_token
from decouple import config as getenv
from datetime import datetime

modulos = configs.get_commands()


class Mal(commands.Cog):
    def __init__(self, bot):
        CLIENT_ID     = getenv('CLIENT_ID')
        CLIENT_SECRET = getenv('CLIENT_SECRET')
        token         = mal_token.get_token(CLIENT_ID, CLIENT_SECRET)
        mal_client    = malclient.Client(access_token=token.access_token, nsfw=True)

        self.client_id     = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.mal_token     = token
        self.mal_client    = mal_client
        self.bot           = bot


    @commands.hybrid_group(aliases=modulos['utility']['mal'])
    async def mal(self, ctx):
        '''...'''
        await ctx.reply('anime')
        

    @mal.command()
    @app_commands.describe(user="...")
    async def user(self, ctx, user : str):
        '''...'''
        self.mal_client.refresh_bearer_token(self.client_id, self.client_secret, self.mal_token.refresh_token)
        search = self.mal_client.get_user_anime_list(user)

        res = ''
        c = 0
        for anime in search:
            res += f'{c}- {anime}\n'
            c += 1

        if len(res) > 2000:
            res = res[:2000]

        #await ctx.channel.send(res)
        await ctx.defer()
        await ctx.reply(res)



async def setup(bot):
    await bot.add_cog(Mal(bot))