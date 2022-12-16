import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class OC_Quit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['_quit'])
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.check_guild)
    async def oc_quit(self, ctx):
        '''Força a parar o bot'''
        settings = configs.get_configs()

        embed=discord.Embed(color=colors.default)
        embed.add_field(name='Status do Bot', value=f'```🔴Offline  |  🏓Ping: {round(self.bot.latency * 1000)}ms```', inline=True)
        await ctx.reply(embed=embed, mention_author=False)
        quit()


async def setup(bot):
    await bot.add_cog(OC_Quit(bot))
 