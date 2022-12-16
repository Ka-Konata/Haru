import discord
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class OC_Enablecommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['_enablecommand'])
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.check_guild)
    async def oc_enablecommand(self, ctx, command : str): #finder
        '''Habilita o uso de algum comando em todos os servidores'''
        settings = configs.get_configs()

        for mod in modulos:
            if command in modulos[mod].keys():
                if command in settings['disabled-commands']:
                    settings['disabled-commands'].remove(command)
                    configs.save(settings, 'storage/configs.json')

                embed = discord.Embed(description=f'O comando `{command}` foi **🔓 HABILITADO** em **todos** os servidores', color=colors.default)
                await ctx.reply(embed=embed, mention_author=False)

                return None
        raise errors.CommandDontExists



async def setup(bot):
    await bot.add_cog(OC_Enablecommand(bot))
 