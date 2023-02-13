from discord.ext import commands
from modules.cog_utility.ui_mal import mal_pagination_view
from math import ceil


anime_status_list = ['watching', 'completed', 'on_hold', 'dropped', 'plan_to_watch', "all"]
anime_sort_dict   = {'update': 'list_updated_at', 'score': 'list_score', 'start': 'anime_start_date', 'title': 'anime_title'}
sort_list         = ['score', 'update', 'title', 'start']


class Cmd:
    async def animelist(parent, ctx, username: str, status: str = 'all', sortedby: str = 'score'):
        await ctx.defer()
        if not sortedby in sort_list or not status in anime_status_list:
            raise commands.errors.BadArgument

        sortedby = anime_sort_dict[sortedby] 
        if status == 'all':
            status = None

        animes = await parent.mal_client.get.anime_list(username, status, sortedby, limit=1000)
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
