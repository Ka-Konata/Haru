import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(aliases=modulos['utility']['avatar'])
    @app_commands.describe(user='Whose profile picture is it', local='Do you want the pfp from the server?')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def avatar(self, ctx, user : discord.Member, local : bool = False):
        '''Download someone's profile picture'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        if local: 
            pfp = user.display_avatar
        else:
            pfp = user.avatar

        embed = discord.Embed(description=lang['COMMAND']['AVATAR']['DESC 1']+str(pfp)+lang['COMMAND']['AVATAR']['DESC 2'], color=colors.default)
        embed.set_image(url=pfp.with_size(512))
        embed.set_author(name=lang['COMMAND']['AVATAR']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['AVATAR']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


    @commands.hybrid_command(aliases=modulos['utility']['banner'])
    @app_commands.describe(user='Whose banner is it')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def banner(self, ctx, user : discord.Member):
        '''Download someone's banner'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        fuser = await self.bot.fetch_user(user.id)
        if fuser.banner == None:
            embed = discord.Embed(description=lang['COMMAND']['BANNER']['DESC NO BANNER 1']+str(fuser.id)+['COMMAND']['BANNER']['DESC NO BANNER 1'], color=colors.default)
        else:
            embed = discord.Embed(description=lang['COMMAND']['BANNER']['DESC 1']+str(fuser.banner)+lang['COMMAND']['BANNER']['DESC 2'], color=colors.default)
            embed.set_image(url=fuser.banner)
        embed.set_author(name=lang['COMMAND']['BANNER']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['BANNER']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


    @commands.hybrid_command(aliases=modulos['utility']['servericon'])
    @app_commands.describe(server='Guild ID')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def servericon(self, ctx, server : discord.Guild = None):
        '''Downloads a guild's icon'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
    
        if server == None:
            server_icon = ctx.guild.icon
        else:
            server_icon = server.icon
        
        embed = discord.Embed(description=lang['COMMAND']['SERVERICON']['DESC 1']+str(server_icon)+lang['COMMAND']['SERVERICON']['DESC 2'], color=colors.default)
        embed.set_image(url=str(server_icon))
        embed.set_author(name=lang['COMMAND']['SERVERICON']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['SERVERICON']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


    @commands.hybrid_command(aliases=modulos['utility']['permissions'])
    @app_commands.describe(member='The one you want to see the permissions')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def permissions(self, ctx, member : discord.Member = None):
        '''Get someone's permissions'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
    
        if member == None:
            member = ctx.author

        perms_aux   = configs.get_perms_as_dict(member.guild_permissions)
        perms_cnt   = 0
        perms_str   = '```'
        for perm_name in  perms_aux.keys():
            if perms_aux[perm_name]:
                try:
                    nm        = lang['PERMISSIONS'][perm_name]
                    perms_str = perms_str + f'{nm}, '
                except KeyError:
                    perms_str = perms_str + f'{perm_name}, '
                perms_cnt += 1
        perms_str = perms_str[0:-2] + '```'

        if perms_cnt == 0:
            perms_str = lang['COMMAND']['PERMISSIONS']['NONE']

        embed = discord.Embed(description=lang['COMMAND']['PERMISSIONS']['DESCRIPTION 1']+member.mention+lang['COMMAND']['PERMISSIONS']['DESCRIPTION 2']+member.top_role.mention, color=colors.default)
        embed.add_field(name=lang['COMMAND']['PERMISSIONS']['PERMS TITLE'], value=perms_str)
        embed.set_author(name=lang['COMMAND']['PERMISSIONS']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['PERMISSIONS']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


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

        mention = '`'+lang['COMMAND']['USERINFO']['USER']['USER']+'`: '+str(user.mention)
        id      = '`'+lang['COMMAND']['USERINFO']['USER']['ID']+'`: '+str(user.id)
        created = '`'+lang['COMMAND']['USERINFO']['USER']['CREATED']+'`: '+str(user.created_at)

        embed = discord.Embed(description=lang['COMMAND']['USERINFO']['DESCRIPTION'], color=colors.default)
        embed.add_field(name=lang['COMMAND']['USERINFO']['USER']['TITLE'], value=f'{mention}\n{id}\n{created}')
        
        member = ctx.guild.get_member(user.id)
        if member != None:

            nick   = '`'+lang['COMMAND']['USERINFO']['MEMBER']['NICK']+'`: '+str(member.nick)
            is_bot = '`'+lang['COMMAND']['USERINFO']['MEMBER']['BOT']+'`: '+lang['COMMAND']['USERINFO']['IS A BOT']['YES'] if member.bot else lang['COMMAND']['USERINFO']['IS A BOT']['NOT']
            joined = '`'+lang['COMMAND']['USERINFO']['MEMBER']['JOINED']+'`: '+str(member.joined_at)
            role   = '`'+lang['COMMAND']['USERINFO']['MEMBER']['ROLE']+'`: '+str(member.top_role.mention)
            roles  = '`'+lang['COMMAND']['USERINFO']['MEMBER']['ROLES']+'`: '+str(member.roles)

            embed.add_field(name=lang['COMMAND']['USERINFO']['MEMBER']['TITLE'], value=f'{nick}\n{is_bot}\n{joined}\n{role}\n{roles}', inline=False)

        
        embed.set_author(name=lang['COMMAND']['USERINFO']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['USERINFO']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Utility(bot))
