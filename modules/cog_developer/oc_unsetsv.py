import typing
import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class OC_Unsetsv(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['_unsetsv'])
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.check_guild)
    async def oc_unsetsv(self, ctx, guild : discord.Guild = None):
        '''Bloqueia o uso do bot no servidor atual'''
        settings = configs.get_configs()

        if guild == None:
            guild_id =  ctx.guild.id
        else:
            guild_id = guild.id

        embed=discord.Embed(color=colors.default)
        if not guild_id in settings['server-list']:
            embed.add_field(name="Resultado:", value="```Servidor não estava na lista.```", inline=True)
        else:
            settings['server-list'].remove(guild_id)
            configs.save(settings)
            embed.add_field(name="Resultado:", value="```Servidor removido.```", inline=True)
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(OC_Unsetsv(bot))
 