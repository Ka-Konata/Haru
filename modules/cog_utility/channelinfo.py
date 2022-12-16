import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class Channelinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(aliases=modulos['utility']['channelinfo'])
    @app_commands.describe(channel='The channel you want to see the informations')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def channelinfo(self, ctx, channel : discord.abc.GuildChannel = None):
        '''Get informations about a channel'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        if channel == None:
            channel = ctx.channel

        created  = '**'+lang['COMMAND']['CHANNELINFO']['CREATED']+'**: `'+channel.created_at.strftime('%d/%m/%Y %H:%M:%S')+'`'
        name     = '**'+lang['COMMAND']['CHANNELINFO']['MENTION']+'**: '+str(channel.mention)
        tipo     = '**'+lang['COMMAND']['CHANNELINFO']['TYPE']['TITLE']+'**: `'+lang['COMMAND']['CHANNELINFO']['TYPE'][str(channel.type)]+'`'
        category = '**'+lang['COMMAND']['CHANNELINFO']['CATEGORY']+'**: '
        category = category+str(channel.category.mention) if channel.category != None else category+'`'+lang['COMMAND']['CHANNELINFO']['NONE']+'`'
        guild    = str(channel.guild.name)+f' `[{channel.guild.id}]`'
        url      = '**'+lang['COMMAND']['CHANNELINFO']['URL']+channel.jump_url+')**'
        
        desc = f'{created}\n{name}\n{tipo}\n{category}\n\n{guild}\n{url}'
        embed = discord.Embed(color=colors.default)
        embed.add_field(name=lang['COMMAND']['CHANNELINFO']['CHANEL TITLE'], value=desc)
        embed.set_author(name=lang['COMMAND']['CHANNELINFO']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['CHANNELINFO']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Channelinfo(bot))
