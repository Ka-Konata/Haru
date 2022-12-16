import discord, requests, typing, malclient
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors, mal_token
from decouple import config as getenv
from datetime import datetime
from math import ceil

modulos     = configs.get_commands()
#sorters     = malclient.MyAnimeListSorting()
status_list = ["watching", "completed", "on_hold", "dropped", "plan_to_watch"]
sort_list   = ['update', 'score', 'start', 'title']
sort_dict   = {'update': 'list_updated_at', 'score': 'list_score', 'start': 'anime_start_date', 'title': 'anime_title'}


class PaginationView(discord.ui.View):


    def __init__(self, *, ctx: commands.Context, timeout: float = 180):
        self.ctx         = ctx
        self.storage     = ''
        self.embeded     = False
        self.user_list   = False
        self.user_name   = ''
        self.pages_f     = 0
        self.pages_t     = 0
        self.page_actual = 0
        self.timedout    = False

        super().__init__(timeout=timeout)


    async def on_timeout(self) -> None:
        self.timedout = True
        self.disable_or_enable_buttons()
        return await super().on_timeout()


    def create_list(self): 
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(self.ctx.guild.id)['language']]
        if self.user_list:
            embed = discord.Embed(title=f'{self.user_name} Anime List\'s (ordened by score)', description=f'page: {self.page_actual}/{self.pages_f} (showing 20 out of {len(self.storage)} anime found)', color=colors.default)
        else:
            embed = discord.Embed()
        c = self.page_actual*20
        res = ''
        animes = self.storage[c:(self.page_actual+1)*20] if len(self.storage) > (self.page_actual+1)*20 else self.storage[c:]
        for anime in animes:
            c += 1
            if self.user_list:
                embed.add_field(name=f'{c}. {anime.title}', value=f'**score: **`{anime.my_list_status.score}`\n**status: **`{anime.my_list_status.status}` `{anime.my_list_status.num_episodes_watched}/{anime.num_episodes}`', inline=False)
            else:
                res = res + f'**{c}.** {anime}\n'
        embed.set_author(name=lang['COMMAND']['CURRENCY']['NAME'], icon_url=settings['bot-icon'])
        # embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['CURRENCY']['FOOTER'])
        return embed


    def disable_or_enable_buttons(self):
        bnt_previous = self.children[0]
        bnt_next = self.children[1]
        print(self.page_actual*20, len(self.storage))
        if self.timedout:
            bnt_next.disabled = True
            bnt_previous.disabled = True
        elif self.page_actual == 0:  # First Page
            bnt_next.disabled = False
            bnt_previous.disabled = True
        elif self.page_actual*20 >= len(self.storage):  # Last Page
            bnt_next.disabled = True
            bnt_previous.disabled = False
        else:  # Any Middle Page
            bnt_next.disabled = False
            bnt_previous.disabled = False


    @discord.ui.button(label='◀️', style=discord.ButtonStyle.gray)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.page_actual -= 1
        anime_list = self.create_list()
        self.disable_or_enable_buttons()
        await self.message.edit(embed=anime_list, view=self)
        await interaction.response.defer()


    @discord.ui.button(label='▶️', style=discord.ButtonStyle.gray)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.page_actual += 1
        anime_list = self.create_list()
        self.disable_or_enable_buttons()
        await self.message.edit(embed=anime_list, view=self)
        await interaction.response.defer()


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
        pass
        

    @mal.command()
    @app_commands.describe(user_name="...")
    async def user(self, ctx, user_name: str, with_status: str = None, sorted_by: str = None):
        '''...'''
        await ctx.defer()
        if not sorted_by in sort_list or with_status in status_list:
            raise commands.errors.BadArgument

        sorted_by = sort_dict[sorted_by] 
        fields = malclient.Fields()
        fields.num_episodes = True
        self.mal_client.refresh_bearer_token(self.client_id, self.client_secret, self.mal_token.refresh_token)
        search = self.mal_client.get_user_anime_list(user_name, limit=1000, fields=fields, sort=sorted_by, status=with_status)

        view = PaginationView(ctx=ctx)
        view.pages_f = ceil(len(search) / 20)
        view.pages_t = len(search)
        view.storage = search
        view.page_actual = 0
        view.user_list   = True
        view.user_name   = user_name
        view.disable_or_enable_buttons()

        anime_list = view.create_list()

        message = await ctx.reply(embed=anime_list, view=view)
        view.message = message
        await view.wait()


    @user.autocomplete('with_status')
    async def command_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for choice in status_list:
            if current.lower() in choice:
                choice_list.append(app_commands.Choice(name=choice, value=choice))
        return choice_list


    @user.autocomplete('sorted_by')
    async def command_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for choice in sort_list:
            if current.lower() in choice:
                choice_list.append(app_commands.Choice(name=choice, value=choice))
        return choice_list




async def setup(bot):
    await bot.add_cog(Mal(bot))


"""AnimeObject = id=1535, 
 title='Death Note', 
 main_picture=Asset(large=HttpUrl('https://api-cdn.myanimelist.net/images/anime/9/9453l.jpg', ), 
 medium=HttpUrl('https://api-cdn.myanimelist.net/images/anime/9/9453.jpg', )), 
 alternative_titles=None, 
 start_date=None, 
 end_date=None, 
 synopsis=None, 
 mean=None, 
 rank=None, 
 popularity=None, 
 num_list_users=None, 
 num_scoring_users=None, 
 nsfw=None, genres=None, 
 created_at=None, 
 updated_at=None, 
 media_type=None, 
 status=None, 
 my_list_status=MyAnimeListStatus(score=10, status='completed', is_rewatching=False, updated_at=datetime.datetime(2022, 9, 15, 14, 52, 33, tzinfo=datetime.timezone.utc), num_episodes_watched=37, start_date=None, finish_date=None), num_episodes=None, start_season=None, broadcast=None, source=None, average_episode_duration=None, rating=None, studios=None, pictures=None, background=None, related_anime=None, related_manga=None, recommendations=None, statistics=None, videos=None),"""
