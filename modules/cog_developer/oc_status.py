import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class OC_Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(aliases=['_stts', '_status'])
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.check_guild)
    async def oc_status(self, ctx):
        '''Envia um hello world, e os status do bot'''
        settings = configs.get_configs()

        embed = discord.Embed(title='', description=f'**User do Bot:** {self.bot.user.mention}\n**ID do bot:** {self.bot.user.id}\n**Iniciado em:** {settings["started-at"]}', color=colors.default)
        embed.set_author(name=settings["bot-name"], icon_url=settings["bot-icon"])
        embed.add_field(name='Status do Bot', value=f'```🟢Online  |  🏓Ping: {round(self.bot.latency * 1000)}ms```', inline=False)
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(OC_Status(bot))
 