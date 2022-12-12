import discord, requests, typing
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors
from decouple import config as getenv
from datetime import datetime

modulos = configs.get_commands()
quotes = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL']


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
            id = str(fuser.id)
            embed = discord.Embed(description=lang['COMMAND']['BANNER']['DESC NO BANNER 1']+id+['COMMAND']['BANNER']['DESC NO BANNER 1'], color=colors.default)
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
            if perms_aux[perm_name] and perm_name != 'value':
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


    @commands.hybrid_command(aliases=modulos['utility']['roleinfo'])
    @app_commands.describe(role='The role you want to see the informations')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def roleinfo(self, ctx, role : discord.Role):
        '''Get informations about a role'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        name = '**'+lang['COMMAND']['ROLELINFO']['MENTION']+'**: '+str(role.mention)
        id = '**'+lang['COMMAND']['ROLELINFO']['ID']+'**: `'+str(role.id)+'`'
        created = '**'+lang['COMMAND']['ROLELINFO']['CREATED']+'**: `'+role.created_at.strftime('%d/%m/%Y %H:%M:%S')+'`'

        desc = f'{name}\n{id}\n{created}'

        perms_aux   = configs.get_perms_as_dict(role.permissions)
        perms_cnt   = 0
        perms_str   = '```'
        for perm_name in perms_aux.keys():
            if perms_aux[perm_name] and perm_name != 'value':
                try:
                    nm        = lang['PERMISSIONS'][perm_name]
                    perms_str = perms_str + f'{nm}, '
                except KeyError:
                    perms_str = perms_str + f'{perm_name}, '
                perms_cnt += 1
        perms_str = perms_str[0:-2] + '```'

        if perms_cnt == 0:
            perms_str = lang['COMMAND']['PERMISSIONS']['NONE']

        embed = discord.Embed(color=colors.default)
        embed.add_field(name=lang['COMMAND']['ROLELINFO']['INFO TITLE'], value=desc)
        embed.add_field(name=lang['COMMAND']['ROLELINFO']['PERMS TITLE'], value=perms_str, inline=False)
        embed.set_author(name=lang['COMMAND']['ROLELINFO']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['ROLELINFO']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


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


    @commands.hybrid_command(aliases=modulos['utility']['currency'])
    @app_commands.describe(original='The original quote', new='The new quote you want to convert to', value='The value you want to convert')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def currency(self, ctx, original : str, new : str, value : float):
        '''Convert a value to another quote'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        api_key = getenv('API_LAYER_KEY')
        url     = f'https://api.apilayer.com/currency_data/convert?to={new.upper()}&from={original.upper()}&amount={value}'

        response = requests.request("GET", url, headers={"apikey": api_key}, data = {})
        response = response.json()

        if not response['success']:
            raise errors.CurrencyApiError

        result = response['result']
        quote  = response['info']['quote']
        time   = datetime.fromtimestamp(response['info']['timestamp'])

        embed = discord.Embed(description=lang['COMMAND']['CURRENCY']['DESC']+': `'+str(time)+'`', color=colors.default)
        embed.add_field(name=lang['COMMAND']['CURRENCY']['F1 TITLE'], value='**{}:** `{:.2f}`'.format(original.upper(), value))
        embed.add_field(name=lang['COMMAND']['CURRENCY']['F2 TITLE'], value='**{}:** `{:.2f}`'.format(new.upper(), result))
        embed.add_field(name=lang['COMMAND']['CURRENCY']['F3 TITLE'], value=f'`{quote}`')
        embed.set_author(name=lang['COMMAND']['CURRENCY']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['CURRENCY']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


    @currency.autocomplete('original')
    @currency.autocomplete('new')
    async def help_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for quote in quotes:
            if current.upper() in quote.upper() and len(choice_list) < 25:
                choice_list.append(app_commands.Choice(name=quote, value=quote))
        return choice_list


    @currency.error
    async def currency_error(self, ctx, error):
        if isinstance(error, errors.CurrencyApiError):
            lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
            embed = errors.get_error_embed(lang, lang['ERROR']['CurrencyApiError']['TYPE'], reason=lang['ERROR']['CurrencyApiError']['REASON'], tip=lang['ERROR']['CurrencyApiError']['TIP'])
        else:
            return None
        await ctx.reply(embed=embed, mention_author=False)


    @commands.hybrid_command(aliases=modulos['utility']['random'])
    @app_commands.describe(until_num='Until the number', from_num='From the number')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def random(self, ctx, from_num : int = 0, until_num : int = 100):
        '''Get a random number'''
        from random import randint
        if from_num >= until_num:
            raise errors.StartBiggerThanEnd

        num = randint(from_num, until_num)
        await ctx.reply(f'`{num}`', mention_author=False)


    @random.error
    async def random_error(self, ctx, error):
        if isinstance(error, errors.StartBiggerThanEnd):
            lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
            embed = errors.get_error_embed(lang, lang['ERROR']['StartBiggerThanEnd']['TYPE'], reason=lang['ERROR']['StartBiggerThanEnd']['REASON'])
        else:
            return None
        await ctx.reply(embed=embed, mention_author=False)


    #@commands.hybrid_group(aliases=modulos['utility']['anime'])
    #async def anime(self, ctx):
    #    '''Get informations about an anime on My Anime List'''
    #    await ctx.reply('anime')
#
#
    #@anime.command()
    #@app_commands.describe(name="Anime's name")
    #@commands.check(configs.Authentication.member)
    #@commands.check(configs.check_islocked)
    #@commands.check(configs.check_guild)
    #async def user(self, ctx, name : str):
    #    '''Get informations about an anime on My Anime List'''
    #    await ctx.reply('anime user')



async def setup(bot):
    await bot.add_cog(Utility(bot))