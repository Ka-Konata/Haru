import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class OC_Listdeveloper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['_listdeveloper'])
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.check_guild)
    async def oc_listdeveloper(self, ctx):
        '''Lista todos os usuários com permissão de manager'''
        settings = configs.get_configs()

        dev_list = settings['developer-list']
        dev_list_str = ''
        c = 0
        for dev in dev_list:
            c += 1
            dev_list_str += ctx.bot.get_user(dev).mention
            if not c == len(dev_list):
                dev_list_str += ', '
        if dev_list_str == '':
            dev_list_str = '`nenhum`'

        embed=discord.Embed(color=colors.default)
        embed.add_field(name="Lista de Developers:", value=dev_list_str, inline=True)
        embed.set_footer(text=f"Total: {len(dev_list)} developer(s)")
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(OC_Listdeveloper(bot))
 