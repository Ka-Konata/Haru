import discord, typing#, myanimelist
from discord import app_commands
from discord.ext import commands
from scripts import configs
from decouple import config as getenv
from modules.cog_utility.ui import mal_pagination_view
from modules.cog_utility.mal_category import user as mal_user
from modules.cog_utility.mal_category import anime as mal_anime
from modules.cog_utility.mal_category import manga as mal_manga
from modules.cog_utility.mal_category import animelist as mal_animelist
from modules.cog_utility.mal_category import mangalist as mal_mangalist
from math import ceil


modulos     = configs.get_commands()
#sorters     = malclient.MyAnimeListSorting()
anime_status_list = ['watching', 'completed', 'on_hold', 'dropped', 'plan_to_watch', "all"]
manga_status_list = ['reading', 'completed', 'on_hold', 'dropped', 'plan_to_read', "all"]
anime_sort_dict   = {'update': 'list_updated_at', 'score': 'list_score', 'start': 'anime_start_date', 'title': 'anime_title'}
manga_sort_dict   = {'score': 'list_score', 'update': 'list_updated_at', 'title': 'manga_title', 'start': 'manga_start_date'} 
sort_list         = ['score', 'update', 'title', 'start']


class Mal(commands.Cog):
    def __init__(self, bot):
        CLIENT_ID     = getenv('CLIENT_ID')
        CLIENT_SECRET = getenv('CLIENT_SECRET')
        ## ATIVAR ESSA LINHA DPS mal_client    = myanimelist.Connect(getenv('CLIENT_ID'))

        self.client_id     = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        ## ATIVAR ESSA LINHA DPS self.mal_client    = mal_client
        self.bot           = bot


    @commands.hybrid_group(aliases=modulos['utility']['mal'])
    async def mal(self, ctx):
        '''...'''
        raise commands.errors.CommandNotFound

    """
    @mal.command()
    @app_commands.describe(username='Must be exactly the same as the username on the website')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def user(self, ctx, username: str):
        '''Serach for someone's profile on MyAnimeList'''
        await mal_user.Cmd.user(self, ctx, username)


    @mal.command()
    @app_commands.describe(anime='Must be exactly the same as the username on the website')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def anime(self, ctx, anime: str):
        '''Serach for any anime on MyAnimeList'''
        await mal_anime.Cmd.anime(self, ctx, anime)


    @mal.command()
    @app_commands.describe(manga='Must be exactly the same as the username on the website')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def manga(self, ctx, manga: str):
        '''Serach for any manga on MyAnimeList'''
        await mal_manga.Cmd.manga(self, ctx, manga)


    @mal.command()
    @app_commands.describe(
        username='Must be exactly the same as the username on the website', 
        status='Search for animes with only one status type', 
        sortedby='How the list will be sorted')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def animelist(self, ctx, username: str, status: str = 'all', sortedby: str = 'score'):
        '''Search for someone's anime list on MyAnimeList'''
        await mal_animelist.Cmd.animelist(self, ctx, username, status, sortedby)


    @animelist.autocomplete('status')
    async def command_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for choice in anime_status_list:
            if current.lower() in choice:
                choice_list.append(app_commands.Choice(name=choice, value=choice))
        return choice_list


    @animelist.autocomplete('sortedby')
    async def command_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for choice in sort_list:
            if current.lower() in choice:
                choice_list.append(app_commands.Choice(name=choice, value=choice))
        return choice_list
        

    @mal.command()
    @app_commands.describe(
        username='Must be exactly the same as the username on the website', 
        status='Search for mangas with only one status type', 
        sortedby='How the list will be sorted')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def mangalist(self, ctx, username: str, status: str = 'all', sortedby: str = 'score'):
        '''Search for someone's manga list on MyAnimeList'''
        await mal_mangalist.Cmd.mangalist(self, ctx, username, status, sortedby)


    @mangalist.autocomplete('status')
    async def command_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for choice in manga_status_list:
            if current.lower() in choice:
                choice_list.append(app_commands.Choice(name=choice, value=choice))
        return choice_list


    @mangalist.autocomplete('sortedby')
    async def command_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for choice in sort_list:
            if current.lower() in choice:
                choice_list.append(app_commands.Choice(name=choice, value=choice))
        return choice_list
    """

async def setup(bot):
    await bot.add_cog(Mal(bot))
