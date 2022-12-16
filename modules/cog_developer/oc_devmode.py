import discord
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class OC_Devmode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['_devmode'])
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.check_guild)
    async def oc_devmode(self, ctx, toggle : str):
        '''Ativa ou desativa o modo de desenvolvimento'''
        settings = configs.get_configs()

        embed=discord.Embed(color=colors.default)
        if toggle == 'on':
            settings['development-mode'] = True
            embed.add_field(name="Modo de Desenvolvedor:", value="```🟢Ativado```", inline=True)
        elif toggle == 'off':
            settings['development-mode'] = False
            embed.add_field(name="Modo de Desenvolvedor:", value="```🔴Desativado```", inline=True)
        else:
            raise errors.DevModeUnknown
        configs.save(settings)
        await ctx.reply(embed=embed, mention_author=False)


    @oc_devmode.error
    async def oc_devmode_error(self, ctx, error):
        if isinstance(error, errors.DevModeUnknown):
            lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
            embed = errors.get_error_embed(lang, 'Modo Desconhecido', tip='Modos conhecidos: on, off')
        else:
            return None
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(OC_Devmode(bot))
 