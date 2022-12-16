import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class OC_Pmtmanager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['_pmtmanager'])
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.check_guild)
    async def oc_pmtmanager(self, ctx, user : discord.User):
        '''Adiciona um usuário na lista de managers'''
        settings = configs.get_configs()

        embed=discord.Embed(color=colors.default)
        if user.id in settings['manager-list'] or user.id in settings['developer-list']:
            embed.add_field(name="Resultado:", value="```Usuário já é um manager ou developer.```", inline=True)
        else:
            settings['manager-list'].append(user.id)
            configs.save(settings)
            embed.add_field(name="Resultado:", value="```Usuário adicionado na lista de managers.```", inline=True)
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(OC_Pmtmanager(bot))
 