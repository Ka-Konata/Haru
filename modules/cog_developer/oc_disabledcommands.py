import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class OC_Disabledcommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['_disabledcommands'])
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.check_guild)
    async def oc_disabledcommands(self, ctx): #finder
        '''Sends a list of all locked commands on this guild'''
        settings = configs.get_configs()
        cmd_list = settings['disabled-commands']
        cmds_str = ''
        for cmd in cmd_list:
            cmds_str = cmds_str+'`'+cmd+'`\t'
        if len(cmd_list) == 0:
            cmds_str = '`nenhum`'

        embed = discord.Embed(description='Lista com todos os comandos desabilitados **globalmente**', color=colors.default)
        embed.add_field(name='Comandos Desabilitados:', value=cmds_str, inline=True)
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(OC_Disabledcommands(bot))
 