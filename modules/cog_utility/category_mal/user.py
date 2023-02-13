import discord, asyncio
from scripts import configs, colors
from modules.cog_utility.ui_mal import mal_profile_view


class Cmd:
    async def user(parent, ctx, username: str):
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        await ctx.defer()
        embed_1 = discord.Embed(color=colors.default)
        embed_1.set_author(name=lang['COMMAND']['MAL USER']['NAME'], icon_url=settings['bot-icon'])
        embed_1.set_footer(text=lang['COMMAND']['MAL USER']['FOOTER'])

        #profile = await asyncio.wait_for(self.mal_client.get.user(username), timeout=1)
        try:
            profile = await asyncio.wait_for(parent.mal_client.get.user(username), timeout=0.1)
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
            embed_1.description = lang['COMMAND']['MAL USER']['LINK']+link+f') \n'+lang['COMMAND']['MAL USER']['LAST ON']+f'`{online}`\n'+lang['COMMAND']['MAL USER']['JOINED']+f'`{joined}`\n\n'+lang['COMMAND']['MAL USER']['DESC 1']
            embed_1.add_field(name='ANIME STATS', value=anime_stat)
            embed_1.add_field(name='MANGA STATS', value=manga_stat)

            embed_2 = discord.Embed(color=colors.default)
            embed_2.set_author(name=lang['COMMAND']['MAL USER']['NAME'], icon_url=settings['bot-icon'])
            embed_2.set_footer(text=lang['COMMAND']['MAL USER']['FOOTER'])
            embed_2.set_thumbnail(url=profile.image)
            embed_2.description = lang['COMMAND']['MAL USER']['LINK']+link+f') \n'+lang['COMMAND']['MAL USER']['LAST ON']+f'`{online}`\n'+lang['COMMAND']['MAL USER']['JOINED']+f'`{joined}`\n\n'+lang['COMMAND']['MAL USER']['DESC 2'] 

            c = 1
            fav_animes = ''
            for anime in profile.favorites.animes:
                fav_animes += f'**{c}.** [{anime.title}](https://myanimelist.net/anime/{anime.id}/)\n'
                c += 1

            c = 1
            fav_mangas = ''
            for manga in profile.favorites.mangas:
                fav_mangas += f'**{c}.** [{manga.title}](https://myanimelist.net/anime/{manga.id}/)\n'
                c += 1

            c = 1
            fav_peoples = ''
            for people in profile.favorites.peoples:
                fav_peoples += f'**{c}.** [{people.name}](https://myanimelist.net/anime/{people.id}/)\n'
                c += 1
                
            c = 1
            fav_characters = ''
            for character in profile.favorites.characters:
                fav_characters += f'**{c}.** [{character.name}](https://myanimelist.net/anime/{character.id}/)\n'
                c += 1

            embed_2.add_field(name=lang['COMMAND']['MAL USER']['ANIME FAVS'], value=fav_animes, inline=False)
            embed_2.add_field(name=lang['COMMAND']['MAL USER']['MANGA FAVS'], value=fav_mangas, inline=False)
            embed_2.add_field(name=lang['COMMAND']['MAL USER']['PEOPLE FAVS'], value=fav_peoples, inline=False)
            embed_2.add_field(name=lang['COMMAND']['MAL USER']['CHARACTER FAVS'], value=fav_characters, inline=False)

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
