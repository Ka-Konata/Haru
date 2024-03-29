import discord
from scripts import configs, colors
from modules.cog_utility.ui import mal_results_view


class Cmd:
    async def anime(parent, ctx, anime: str):
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]['COMMAND']['MAL ANIME']
        await ctx.defer()     

        options  = list()
        callback = dict()

        result = await parent.mal_client.search.anime(anime)
        for anime in result:
            options.append(discord.SelectOption(label=anime.title))

            embed = discord.Embed(color=colors.default, title=f'**{anime.title}**')
            embed.set_author(name=lang['NAME'], icon_url=settings['bot-icon'])
            embed.set_footer(text=lang['FOOTER'])
            embed.set_image(url=str(anime.image))

            nsfw              = ' | **nsfw**' if anime.nsfw == 'black' else ''
            embed.description = lang['DESC']+f'(https://myanimelist.net/anime/{anime.id})'+nsfw

            titles     = ''
            titles     = titles + f'`{anime.en_title}` ' if anime.en_title != None else ''
            titles     = titles + f'\n`{anime.ja_title}`' if anime.ja_title != None else ''
            date       = f' `{anime.start_date.replace("-", "/") if anime.start_date != None else "?"}` - `{anime.end_date.replace("-", "/") if anime.end_date != None else "?"}`'
            popularity = f' `#{anime.popularity}`'
            list_users = f' `{anime.num_list_users}`'

            embed.add_field(name=lang['RANK']+f'#{anime.rank} (:star: {anime.mean} - {anime.num_scoring_users} members)', value=lang['EMBED 1']+date+lang['EMBED 3']+popularity+lang['EMBED 4']+list_users+lang['EMBED 2']+titles)

            callback[anime.title] = embed

        placeholder = lang['PLACEHOLDER']
        select_menu = mal_results_view.Select(options, callback, placeholder)
        view        = mal_results_view.SelectView(ctx, select_menu)

        await ctx.reply(lang['RESULTS'], view=view, mention_author=False)
        await view.wait()
 