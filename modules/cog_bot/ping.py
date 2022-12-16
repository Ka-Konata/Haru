from discord.ext import commands
from scripts import configs

modulos = configs.get_commands()
categories = {
    "help": ['view', 'command', 'module']
}


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot


    @commands.hybrid_command(aliases=modulos['bot']['ping'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def ping(self, ctx):
        '''Used to know if haru is alive team'''

        await ctx.reply(f'`🏓Pong ({round(self.bot.latency * 1000)}ms)`', mention_author=False)


async def setup(bot):
    await bot.add_cog(Ping(bot))
 