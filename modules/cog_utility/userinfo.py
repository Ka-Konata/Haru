import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(aliases=modulos['utility']['userinfo'])
    @app_commands.describe(user='The one you want to see the informations')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def userinfo(self, ctx, user : discord.User = None):
        '''Get someone's basic informations'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
    
        if user == None:
            user = ctx.author

        mention = '**'+lang['COMMAND']['USERINFO']['USER']['USER']+ '**: '+str(user.mention)
        id      = '**'+lang['COMMAND']['USERINFO']['USER']['ID']+ '**: `'+str(user.id)+'`'
        created = '**'+lang['COMMAND']['USERINFO']['USER']['CREATED']+ '**: `'+str(user.created_at.strftime('%d/%m/%Y %H:%M:%S'))+'`'

        embed = discord.Embed(color=colors.default)
        embed.add_field(name=lang['COMMAND']['USERINFO']['USER']['TITLE'], value=f'{mention}\n{id}\n{created}')
        
        member = ctx.guild.get_member(user.id)
        if member != None:
            roles_list = ''
            for r in member.roles:
                roles_list = roles_list + '' + str(r.mention) + '\t'

            nick   = '**'+lang['COMMAND']['USERINFO']['MEMBER']['NICK']+ '**: `'+str(member.nick)+'`'
            is_bot = '**'+lang['COMMAND']['USERINFO']['MEMBER']['BOT']+ '**: `'
            is_bot = is_bot+lang['COMMAND']['USERINFO']['IS A BOT']['YES']+'`' if member.bot else is_bot+lang['COMMAND']['USERINFO']['IS A BOT']['NOT']+'`'
            joined = '**'+lang['COMMAND']['USERINFO']['MEMBER']['JOINED']+ '**: `'+str(member.joined_at.strftime('%d/%m/%Y %H:%M:%S'))+'`'
            role   = '**'+lang['COMMAND']['USERINFO']['MEMBER']['ROLE']+ '**: '+str(member.top_role.mention)
            roles  = '**'+lang['COMMAND']['USERINFO']['MEMBER']['ROLES']+ '**: '+str(roles_list)

            embed.add_field(name=lang['COMMAND']['USERINFO']['MEMBER']['TITLE'], value=f'{nick}\n{is_bot}\n{joined}\n{role}\n{roles}', inline=False)

        
        embed.set_author(name=lang['COMMAND']['USERINFO']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=user.avatar)
        embed.set_footer(text=lang['COMMAND']['USERINFO']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Userinfo(bot))
 