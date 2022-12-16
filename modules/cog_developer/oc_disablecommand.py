import discord
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class OC_Disablecommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['_disablecommand'])
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.check_guild)
    async def oc_disablecommand(self, ctx, command : str):
        '''Desabilita o uso de algum comando em todos os servidores'''
        settings = configs.get_configs()

        for mod in modulos:
            if command in modulos[mod].keys():
                if mod in ['configuration']:
                    print('cannot', mod)
                    raise errors.CannotBeLocked

                if not command in settings['disabled-commands']:
                    settings['disabled-commands'].append(command)
                    configs.save(settings, 'storage/configs.json')

                embed = discord.Embed(description=f'O comando `{command}` foi **🔐 DESABILITADO** em **todos** os servidores.', color=colors.default)

                await ctx.reply(embed=embed, mention_author=False)

                return None
        raise errors.CommandDontExists


async def setup(bot):
    await bot.add_cog(OC_Disablecommand(bot))
 