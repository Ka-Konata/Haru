import discord
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class OC_Disablemodule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['_disablemodule'])
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def oc_disablemodule(self, ctx, module : str):
        '''Desabilita o uso de algum módulo em todos os servidores'''
        settings = configs.get_configs()

        if module in ['configuration']:
            print('cannot', mod)
            raise errors.CannotBeLocked

        for mod in modulos:
            if mod == module:
                cmds_str = ''
                guild = configs.get_guild(ctx.guild.id, all=True)
                for cmd in modulos[module].keys():
                    cmds_str = cmds_str+'`'+cmd+'`\t'
                    if not cmd in settings['disabled-commands']:
                        settings['disabled-commands'].append(cmd)
                configs.save(settings, 'storage/configs.json')

                embed = discord.Embed(description=f'Todos os comandos do módulo `{module}` foram ** 🔐 DESABILITADOS** globalmente', color=colors.default)
                embed.add_field(name='Lista de Comandos do Módulo:', value=cmds_str, inline=False)

                await ctx.reply(embed=embed, mention_author=False)

                return None
        raise errors.ModuleDontExists


async def setup(bot):
    await bot.add_cog(OC_Disablemodule(bot))
 