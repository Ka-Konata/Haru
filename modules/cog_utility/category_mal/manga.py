import discord
from scripts import configs, colors
from modules.cog_utility.ui_mal import mal_results_view


class Cmd:
    async def manga(parent, ctx, manga: str):
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]['COMMAND']['MAL MANGA']
        await ctx.defer()     

        options  = list()
        callback = dict()

        result = await parent.mal_client.search.manga(manga)
        for manga in result:
            options.append(discord.SelectOption(label=manga.title))

            embed = discord.Embed(color=colors.default, title=f'**{manga.title}**')
            embed.set_author(name=lang['NAME'], icon_url=settings['bot-icon'])
            embed.set_footer(text=lang['FOOTER'])
            embed.set_image(url=str(manga.image))

            nsfw              = ' | **nsfw**' if manga.nsfw == 'black' else ''
            embed.description = lang['DESC']+f'(https://mymangalist.net/manga/{manga.id})'+nsfw

            titles     = ''
            titles     = titles + f'`{manga.en_title}` ' if manga.en_title != None else ''
            titles     = titles + f'\n`{manga.ja_title}`' if manga.ja_title != None else ''
            date       = f' `{manga.start_date.replace("-", "/") if manga.start_date != None else "?"} - {manga.end_date.replace("-", "/") if manga.end_date != None else "?"}`'
            popularity = f' `#{manga.popularity}`'
            list_users = f' `{manga.num_list_users}`'

            embed.add_field(name=lang['RANK']+f'#{manga.rank} (:star: {manga.mean} - {manga.num_scoring_users} members)', value=lang['EMBED 1']+date+lang['EMBED 3']+popularity+lang['EMBED 4']+list_users+lang['EMBED 2']+titles)

            callback[manga.title] = embed

        placeholder = lang['PLACEHOLDER']
        select_menu = mal_results_view.Select(options, callback, placeholder)
        view        = mal_results_view.SelectView(ctx, select_menu)

        await ctx.reply(lang['RESULTS'], view=view, mention_author=False)
        await view.wait()
 