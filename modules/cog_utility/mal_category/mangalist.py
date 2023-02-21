from discord.ext import commands
from modules.cog_utility.ui import mal_pagination_view
from math import ceil


manga_status_list = ['reading', 'completed', 'on_hold', 'dropped', 'plan_to_read', "all"]
manga_sort_dict   = {'score': 'list_score', 'update': 'list_updated_at', 'title': 'manga_title', 'start': 'manga_start_date'} 
sort_list         = ['score', 'update', 'title', 'start']


class Cmd:
    async def mangalist(parent, ctx, username: str, status: str = 'all', sortedby: str = 'score'):
        await ctx.defer()
        if not sortedby in sort_list or not status in manga_status_list:
            raise commands.errors.BadArgument

        sortedby = manga_sort_dict[sortedby] 
        if status == 'all':
            status = None

        mangas = await parent.mal_client.get.manga_list(username, status, sortedby, limit=1000)
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
