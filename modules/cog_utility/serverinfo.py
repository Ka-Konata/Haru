import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(aliases=modulos['utility']['serverinfo'])
    @app_commands.describe(guild_id='The server you want to see the informations')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def serverinfo(self, ctx, guild_id : discord.Guild = None):
        '''Get informations about a guild'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        if guild_id == None:
            guild = ctx.guild
        else:
            guild = guild_id

        name = '**'+lang['COMMAND']['SERVERINFO']['MENTION']+'**: '+str(guild.name)
        id = '**'+lang['COMMAND']['SERVERINFO']['ID']+'**: `'+str(guild.id)+'`'
        created = '**'+lang['COMMAND']['SERVERINFO']['CREATED']+'**: `'+guild.created_at.strftime('%d/%m/%Y %H:%M:%S')+'`'
        owner = '**'+lang['COMMAND']['SERVERINFO']['OWNER']+'**: '+guild.owner.mention
        icon = str(guild.icon)
        roles_c = '**'+lang['COMMAND']['SERVERINFO']['ROLES']+'**: `'+str(len(guild.roles))+'`'
        channel_text = '**'+lang['COMMAND']['SERVERINFO']['TEXT']+'**: `'+str(len(guild.text_channels))+'`'
        channel_voice = '**'+lang['COMMAND']['SERVERINFO']['VOICE']+'**: `'+str(len(guild.voice_channels))+'`'
        member_c = '**'+lang['COMMAND']['SERVERINFO']['MEMBERS']+'**: `'+str(guild.member_count)+'`'
        booster_c = '**'+lang['COMMAND']['SERVERINFO']['BOOSTERS']+'**: `'+str(guild.premium_subscription_count)+'`'
        if guild.description != None:
            desc = '**'+lang['COMMAND']['SERVERINFO']['DESC']+'**: ```'+guild.description+'```'
        else:
            desc = '**'+lang['COMMAND']['SERVERINFO']['DESC']+'**: '+lang['COMMAND']['PERMISSIONS']['NONE']

        f1 = f'{name}\n{id}\n{created}\n{owner}'
        f2 = f'{roles_c}\n{channel_text}\n{channel_text}\n{member_c}\n{booster_c}'

        embed = discord.Embed(description=desc, color=colors.default)
        embed.add_field(name=lang['COMMAND']['SERVERINFO']['F1 TITLE'], value=f1, inline=True)
        embed.add_field(name=lang['COMMAND']['SERVERINFO']['F2 TITLE'], value=f2, inline=True)
        embed.set_author(name=lang['COMMAND']['SERVERINFO']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=icon)
        embed.set_footer(text=lang['COMMAND']['SERVERINFO']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Serverinfo(bot))
 