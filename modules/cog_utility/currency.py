import discord, requests, typing
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors
from decouple import config as getenv
from datetime import datetime

modulos = configs.get_commands()
quotes = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL']


class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


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


async def setup(bot):
    await bot.add_cog(Currency(bot))
