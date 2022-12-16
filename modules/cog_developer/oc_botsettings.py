import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class OC_Botsettings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['_botsettings'])
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.check_guild)
    async def oc_botsettings(self, ctx): 
        '''Lista todas as configurações do bot'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        guild = configs.get_guild(ctx.guild.id)

        prefix         = settings['default-prefix']
        language       = settings['default-language']
        devmode        = '🟢On' if settings['development-mode'] else '🔴Off'
        errorsmode     = '🟢On' if settings['errors-mode'] else '🔴Off'
        lockedcommands = ''
        for cmd in settings['disabled-commands']:
            lockedcommands = lockedcommands+'`'+cmd+'`\t'
        if len(settings['disabled-commands']) == 0:
            lockedcommands = '`nenhum`'

        embed = discord.Embed(description='', color=colors.default)
        embed.set_author(name='Informações e Configurações Padrão', icon_url=settings['bot-icon'])
        embed.add_field(name='Informações do Bot:', value=f'**User:** {self.bot.user.mention}\n**ID:** {self.bot.user.id}\n**Iniciado em:** {settings["started-at"]}', inline=True)
        embed.add_field(name='Status do Bot', value=f'```🟢Online\n🏓Ping: {round(self.bot.latency * 1000)}ms```', inline=True)
        embed.add_field(name='Configurações Padrão', value=f'```prefixo: {prefix}\nidioma: {language}```', inline=True)
        embed.add_field(name='Modos Especiais', value=f'```Desenvolvimento: {devmode} \nDebug de Erros: {errorsmode}```', inline=True)
        embed.add_field(name='Comandos Desabilitados Globalmente', value=lockedcommands, inline=True)

        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(OC_Botsettings(bot))
 