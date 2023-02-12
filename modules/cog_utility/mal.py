import discord, requests, typing, malclient, myanimelist, asyncio
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors, mal_token
from decouple import config as getenv
from datetime import datetime
from modules.cog_utility.ui import mal_profile_view, mal_pagination_view
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
        #token         = mal_token.get_token(CLIENT_ID, CLIENT_SECRET)
        #mal_client    = malclient.Client(access_token=token.access_token, nsfw=True)
        mal_client    = myanimelist.Connect(getenv('CLIENT_ID'))

        self.client_id     = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        #self.mal_token     = token
        self.mal_client    = mal_client
        self.bot           = bot


    @commands.hybrid_group(aliases=modulos['utility']['mal'])
    async def mal(self, ctx):
        '''...'''
        raise commands.errors.CommandNotFound


    @mal.command()
    @app_commands.describe(username='Must be exactly the same as the username on the website')
    async def user(self, ctx, username: str):
        '''Serach for someone's profile on MyAnimeList'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        await ctx.defer()
        embed_1 = discord.Embed(color=colors.default)
        embed_1.set_author(name=lang['COMMAND']['MAL USER']['NAME'], icon_url=settings['bot-icon'])
        embed_1.set_footer(text=lang['COMMAND']['MAL USER']['FOOTER'])

        #profile = await asyncio.wait_for(self.mal_client.get.user(username), timeout=1)
        try:
            profile = await asyncio.wait_for(self.mal_client.get.user(username), timeout=0.1)
        except asyncio.TimeoutError:
            embed_1.description = lang['COMMAND']['MAL USER']['TIMEOUT']
            await ctx.reply(embed=embed_1, mention_author=False)

        if profile != None:

            link   = profile.url
            online = profile.last_online.strftime('%d/%m/%Y') if profile.last_online != None else 'N/A'
            joined = profile.joined.strftime('%d/%m/%Y') if profile.joined != None else 'N/A'

            anime_stat  = lang['COMMAND']['MAL USER']['ANIME STAT']['days_watched']+str(profile.statistics.animes.days_watched)+'`\n'
            anime_stat += lang['COMMAND']['MAL USER']['ANIME STAT']['mean_score']+str(profile.statistics.animes.mean_score)+'`\n\n'
            anime_stat += lang['COMMAND']['MAL USER']['ANIME STAT']['watching']+str(profile.statistics.animes.watching)+'`\n'
            anime_stat += lang['COMMAND']['MAL USER']['ANIME STAT']['completed']+str(profile.statistics.animes.completed)+'`\n'
            anime_stat += lang['COMMAND']['MAL USER']['ANIME STAT']['on_hold']+str(profile.statistics.animes.on_hold)+'`\n'
            anime_stat += lang['COMMAND']['MAL USER']['ANIME STAT']['dropped']+str(profile.statistics.animes.dropped)+'`\n'
            anime_stat += lang['COMMAND']['MAL USER']['ANIME STAT']['plan_to_watch']+str(profile.statistics.animes.plan_to_watch)+'`\n\n'
            anime_stat += lang['COMMAND']['MAL USER']['ANIME STAT']['total_entries']+str(profile.statistics.animes.total_entries)+'`\n'
            anime_stat += lang['COMMAND']['MAL USER']['ANIME STAT']['rewatched']+str(profile.statistics.animes.rewatched)+'`\n'
            anime_stat += lang['COMMAND']['MAL USER']['ANIME STAT']['episodes_watched']+str(profile.statistics.animes.episodes_watched)+'`'
            anime_stat  = anime_stat.replace('None', 'N/A')

            manga_stat  = lang['COMMAND']['MAL USER']['MANGA STAT']['days_read']+str(profile.statistics.mangas.days_read)+'`\n'
            manga_stat += lang['COMMAND']['MAL USER']['MANGA STAT']['mean_score']+str(profile.statistics.mangas.mean_score)+'`\n\n'
            manga_stat += lang['COMMAND']['MAL USER']['MANGA STAT']['reading']+str(profile.statistics.mangas.reading)+'`\n'
            manga_stat += lang['COMMAND']['MAL USER']['MANGA STAT']['completed']+str(profile.statistics.mangas.completed)+'`\n'
            manga_stat += lang['COMMAND']['MAL USER']['MANGA STAT']['on_hold']+str(profile.statistics.mangas.on_hold)+'`\n'
            manga_stat += lang['COMMAND']['MAL USER']['MANGA STAT']['dropped']+str(profile.statistics.mangas.dropped)+'`\n'
            manga_stat += lang['COMMAND']['MAL USER']['MANGA STAT']['plan_to_read']+str(profile.statistics.mangas.plan_to_read)+'`\n\n'
            manga_stat += lang['COMMAND']['MAL USER']['MANGA STAT']['total_entries']+str(profile.statistics.mangas.total_entries)+'`\n'
            manga_stat += lang['COMMAND']['MAL USER']['MANGA STAT']['reread']+str(profile.statistics.mangas.reread)+'`\n'
            manga_stat += lang['COMMAND']['MAL USER']['MANGA STAT']['chapters_read']+str(profile.statistics.mangas.chapters_read)+'`\n'
            manga_stat += lang['COMMAND']['MAL USER']['MANGA STAT']['volumes_read']+str(profile.statistics.mangas.volumes_read)+'`'
            manga_stat  = manga_stat.replace('None', 'N/A')

            embed_1.set_thumbnail(url=profile.image)
            embed_1.title = f'**{profile.username}** `id: {profile.id}`\n'
            embed_1.description = lang['COMMAND']['MAL USER']['LINK']+link+f') \n'+lang['COMMAND']['MAL USER']['LAST ON']+f'`{online}`\n'+lang['COMMAND']['MAL USER']['JOINED']+f'`{joined}`'
            embed_1.add_field(name='ANIME STATS', value=anime_stat)
            embed_1.add_field(name='MANGA STATS', value=manga_stat)

            embed_2 = discord.Embed(color=colors.default)
            embed_2.set_author(name=lang['COMMAND']['MAL USER']['NAME'], icon_url=settings['bot-icon'])
            embed_2.set_footer(text=lang['COMMAND']['MAL USER']['FOOTER'])
            embed_2.set_thumbnail(url=profile.image)
            embed_2.description = embed_1.description 

            view             = mal_profile_view.ProfileView(ctx=ctx)
            view.page_actual = 0
            view.ctx         = ctx
            view.embeds.append(embed_1)
            view.embeds.append(embed_2)
            view.disable_or_enable_buttons()

            message = await ctx.reply(embed=embed_1, view=view, mention_author=False)
            view.message = message
            await view.wait()

        else:
            embed_1.description = lang['COMMAND']['MAL USER']['DESC']
            await ctx.reply(embed=embed_1, mention_author=False)
        

    @mal.command()
    @app_commands.describe(
        username='Must be exactly the same as the username on the website', 
        status='Search for animes with only one status type', 
        sortedby='How the list will be sorted')
    async def animelist(self, ctx, username: str, status: str = 'all', sortedby: str = 'score'):
        '''Search for someone's anime list on MyAnimeList'''

        await ctx.defer()
        if not sortedby in sort_list or not status in anime_status_list:
            raise commands.errors.BadArgument

        sortedby = anime_sort_dict[sortedby] 
        if status == 'all':
            status = None

        animes = await self.mal_client.get.anime_list(username, status, sortedby, limit=1000)
        res = ""
        for anime in animes:
            res += f"\n {anime.title}"

        view             = mal_pagination_view.PaginationView(ctx=ctx)
        view.pages       = ceil(len(animes) / 20)
        view.storage     = animes
        view.page_actual = 0
        view.user_list   = True
        view.list_type   = 'anime'
        view.username   = username
        view.disable_or_enable_buttons()

        anime_list = view.create_list()

        message = await ctx.reply(embed=anime_list, view=view, mention_author=False)
        view.message = message
        await view.wait()


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
    async def mangalist(self, ctx, username: str, status: str = 'all', sortedby: str = 'score'):
        '''Search for someone's manga list on MyAnimeList'''

        await ctx.defer()
        if not sortedby in sort_list or not status in manga_status_list:
            raise commands.errors.BadArgument

        sortedby = manga_sort_dict[sortedby] 
        if status == 'all':
            status = None

        mangas = await self.mal_client.get.manga_list(username, status, sortedby, limit=1000)
        res = ""
        for manga in mangas:
            res += f"\n {manga.title}"

        view             = mal_pagination_view.PaginationView(ctx=ctx)
        view.pages       = ceil(len(mangas) / 20)
        view.storage     = mangas
        view.page_actual = 0
        view.user_list   = True
        view.list_type   = 'manga'
        view.username    = username
        view.disable_or_enable_buttons()

        manga_list = view.create_list()

        message = await ctx.reply(embed=manga_list, view=view, mention_author=False)
        view.message = message
        await view.wait()


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


async def setup(bot):
    await bot.add_cog(Mal(bot))
