import discord, requests, typing, malclient
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors, mal_token
from decouple import config as getenv
from datetime import datetime
from math import ceil

modulos     = configs.get_commands()
#sorters     = malclient.MyAnimeListSorting()
status_list = ["watching", "completed", "on_hold", "dropped", "plan_to_watch", "all"]
sort_list   = ['update', 'score', 'start', 'title']
sort_dict   = {'update': 'list_updated_at', 'score': 'list_score', 'start': 'anime_start_date', 'title': 'anime_title'}


class PaginationView(discord.ui.View):


    def __init__(self, *, ctx: commands.Context, timeout: float = 180):
        self.ctx         = ctx
        self.storage     = ''
        self.embeded     = False
        self.user_list   = False
        self.username   = ''
        self.pages       = 0
        self.page_actual = 0
        self.interaction = None

        super().__init__(timeout=timeout)


    async def on_timeout(self) -> None:
        for btn in self.children:
            btn.disabled = True
        await self.message.edit(embed=self.create_list(), view=self)


    def create_list(self): 
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(self.ctx.guild.id)['language']]['COMMAND']['MAL USER_ANIME_LIST']
        if self.user_list:
            embed = discord.Embed(description=lang['TITLE 1']+self.username+f'](https://myanimelist.net/profile/{self.username})'+lang['TITLE 2']+f'{self.page_actual+1}/{self.pages} ({len(self.storage)}'+lang['TITLE 3'], color=colors.default)
        else:
            embed = discord.Embed()

        if self.embeded:
            item = self.storage[self.page_actual]
            embed.title = f'{item.title}'
            embed.description = lang['EMBED 1']+f'(https://myanimelist.net/anime/{item.id}) | '+lang['EMBED 2']+f'(https://myanimelist.net/profile/{self.username})'
            embed.set_image(url=str(item.main_picture.medium))
            if self.user_list:
                embed.add_field(name=lang['EMBED']['RANK']+f'{item.rank} ({item.mean})', value=lang['EMBED']['SCORE']+f'`{item.my_list_status.score}`\n'+lang['EMBED']['STATUS']+f'`{item.my_list_status.status}` `{item.my_list_status.num_episodes_watched}/{item.num_episodes}`')
            else:
                pass
        else:
            c = self.page_actual*20
            res = ''
            animes = self.storage[c:(self.page_actual+1)*20] if len(self.storage) > (self.page_actual+1)*20 else self.storage[c:]
            for anime in animes:
                #print(animes)
                #break

                c += 1
                if self.user_list:
                    score  = 'N/A'
                    status = 'N/A'
                    eps_wt = 'N/A'
                    if anime.my_list_status != None:
                        score  = anime.my_list_status.score
                        status = anime.my_list_status.status
                        eps_wt = anime.my_list_status.num_episodes_watched
                    else:
                        print('Nonetype', anime)

                    embed.add_field(name=f'{c}. {anime.title}', value=lang['LIST']+f'(https://myanimelist.net/anime/{anime.id}) \n'+lang['EMBED']['SCORE']+f'`{score}`\n'+lang['EMBED']['STATUS']+f'`{status}` `{eps_wt}/{anime.num_episodes}`', inline=False)
                else:
                    res = res + f'**{c}.** {anime}\n'
        embed.set_footer(text=lang['FOOTER 1']+f'{self.page_actual}/{self.pages} | '+lang['FOOTER 2'])
        return embed


    def disable_or_enable_buttons(self):
        btn_previous = self.children[0]
        btn_next     = self.children[2]
        if self.page_actual == 0:  # First Page
            btn_next.disabled = False
            btn_previous.disabled = True
        elif self.page_actual == self.pages-1:  # Last Page
            btn_next.disabled = True
            btn_previous.disabled = False
        else:  # Any Middle Page
            btn_next.disabled = False
            btn_previous.disabled = False

    
    async def actualize_embed(self, interaction: discord.Interaction = None):
        anime_list = self.create_list()
        self.disable_or_enable_buttons()
        await interaction.response.edit_message(embed=anime_list, view=self)


    @discord.ui.button(label='◀️', style=discord.ButtonStyle.gray)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.page_actual -= 1
        await self.actualize_embed(interaction)


    @discord.ui.button(label='📖 Change View', style=discord.ButtonStyle.gray)
    async def change_vizualization(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.embeded:
            self.embeded = False
            self.pages = ceil(len(self.storage) / 20)
        else:
            self.embeded = True
            self.pages = len(self.storage)
        self.page_actual = 0
        await self.actualize_embed(interaction)


    @discord.ui.button(label='▶️', style=discord.ButtonStyle.gray)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.page_actual += 1
        await self.actualize_embed(interaction)


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
        raise commands.errors.CommandNotFound
        

    @mal.command()
    @app_commands.describe(
        username='Must be exactly the same as the username on the website', 
        status='Search for animes with only one status type', 
        sortedby='How the list will be sorted')
    async def animelist(self, ctx, username: str, status: str = 'all', sortedby: str = 'score'):
        '''Search for someone's anime list on MyAnimeList'''
        await ctx.defer()
        if not sortedby in sort_list or not status in status_list:
            raise commands.errors.BadArgument

        sortedby = sort_dict[sortedby] 
        if status == 'all':
            status = None

        fields__ = malclient.ListStatusFields()
        fields__.status = fields__.score = fields__.num_episodes_watched = True
        fields = malclient.Fields()
        fields.num_episodes = fields.rank = fields.main_picture = fields.mean = True
        self.mal_client.refresh_bearer_token(self.client_id, self.client_secret, self.mal_token.refresh_token)
        search = self.mal_client.get_user_anime_list(username, limit=1000, fields=fields, list_status_fields=fields__, sort=sortedby, status=status)

        view             = PaginationView(ctx=ctx)
        view.pages       = ceil(len(search) / 20)
        view.storage     = search
        view.page_actual = 0
        view.user_list   = True
        view.username   = username
        view.disable_or_enable_buttons()

        anime_list = view.create_list()

        message = await ctx.reply(embed=anime_list, view=view, mention_author=False)
        view.message = message
        await view.wait()


    @animelist.autocomplete('status')
    async def command_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for choice in status_list:
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


async def setup(bot):
    await bot.add_cog(Mal(bot))


"""id=19, 
title='Monster', 
main_picture=Asset(large=HttpUrl('https://api-cdn.myanimelist.net/images/anime/10/18793l.jpg', ), medium=HttpUrl('https://api-cdn.myanimelist.net/images/anime/10/18793.jpg', )), 
alternative_titles=None, 
start_date=None, 
end_date=None, 
synopsis=None, 
mean=8.85, 
rank=23, 
popularity=None, 
num_list_users=None, 
num_scoring_users=None, 
nsfw=None, genres=None, created_at=None, 
updated_at=None, media_type=None, status=None, 
my_list_status=MyAnimeListStatus(score=0, status='on_hold', is_rewatching=False, updated_at=datetime.datetime(2022, 9, 15, 15, 2, 15, tzinfo=datetime.timezone.utc), num_episodes_watched=5, start_date=None, finish_date=None), num_episodes=74, start_season=None, broadcast=None, source=None, average_episode_duration=None, rating=None, studios=None, pictures=None, background=None, related_anime=None, related_manga=None, recommendations=None, statistics=None, videos=None"""
