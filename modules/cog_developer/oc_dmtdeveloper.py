import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class OC_Dmtdeveloper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['_dmtdeveloper'])
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.check_guild)
    async def oc_dmtdeveloper(self, ctx, user : discord.User):
        '''Adiciona um usuário na lista de managers'''
        settings = configs.get_configs()

        embed=discord.Embed(color=colors.default)
        if not user.id in settings['developer-list']:
            embed.add_field(name="Resultado:", value="```Usuário não estava na lista.```", inline=True)
        else:
            settings['developer-list'].remove(user.id)
            configs.save(settings)
            embed.add_field(name="Resultado:", value="```Usuário removido da lista de developers.```", inline=True)
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(OC_Dmtdeveloper(bot))
 