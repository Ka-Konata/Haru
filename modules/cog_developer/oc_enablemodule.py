import discord
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class OC_Enablemodule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['_enablemodule'])
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.check_guild)
    async def oc_enablemodule(self, ctx, module : str): 
        '''Habilita o uso de algum módulo em todos os servidores'''
        settings = configs.get_configs()

        for mod in modulos:
            if module == mod:
                cmds_str = ''
                for cmd in modulos[mod].keys():
                    cmds_str = cmds_str+'`'+cmd+'`\t'
                    if cmd in settings['disabled-commands']:
                        settings['disabled-commands'].remove(cmd)
                configs.save(settings, 'storage/configs.json')

                embed = discord.Embed(description=f'Todos os comandos do módulo `{module}` foram ** 🔓 HABILITADOS** globalmente', color=colors.default)
                embed.add_field(name='Lista de Comandos do Módulo:', value=cmds_str, inline=False)

                await ctx.reply(embed=embed, mention_author=False)

                return None
        raise errors.ModuleDontExists


async def setup(bot):
    await bot.add_cog(OC_Enablemodule(bot))
 