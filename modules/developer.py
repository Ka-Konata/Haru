import discord
from discord.ext import commands
from scripts import configs, errors, colors

class Developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(aliases=['oc_stts'])
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.guild_check)
    async def oc_status(self, ctx):
        '''Envia um hello world, e os status do bot'''
        settings = configs.get()

        embed = discord.Embed(title='', description=f'**User do Bot:** {self.bot.user.mention}\n**ID do bot:** {self.bot.user.id}\n**Iniciado em:** {settings["started-at"]}', color=colors.default)
        embed.set_author(name=settings["bot-name"], icon_url=settings["bot-icon"])
        embed.add_field(name='Status do Bot', value=f'```🟢Online  |  🏓Ping: {round(self.bot.latency * 1000)}ms```', inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.guild_check)
    async def oc_quit(self, ctx):
        '''Força a parar o bot'''
        settings = configs.get()

        embed=discord.Embed(color=colors.default)
        embed.add_field(name='Status do Bot', value=f'```🔴Offline  |  🏓Ping: {round(self.bot.latency * 1000)}ms```', inline=True)
        await ctx.send(embed=embed)
        quit()
 

    @commands.command()
    @commands.check(configs.Authentication.manager)
    async def oc_setsv(self, ctx, guild : discord.Guild = None):
        '''Libera o uso do bot no servidor atual'''
        settings = configs.get()

        if guild == None:
            guild_id =  ctx.guild.id
        else:
            guild_id = guild.id

        embed=discord.Embed(color=colors.default)
        if guild_id in settings['server-list']:
            embed.add_field(name="Resultado:", value="```Servidor já cadastrado.```", inline=True)
        else:
            settings['server-list'].append(guild_id)
            configs.save(settings)
            embed.add_field(name="Resultado:", value="```Servidor adicionado.```", inline=True)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.guild_check)
    async def oc_unsetsv(self, ctx, guild : discord.Guild = None):
        '''bloqueia o uso do bot no servidor atual'''
        settings = configs.get()

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
        await ctx.send(embed=embed)


    @commands.command()
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.guild_check)
    async def oc_listsv(self, ctx):
        '''lista todos os servidores liberados'''
        settings = configs.get()

        sv_list = settings['server-list']
        sv_list_str = '```'
        c = 1
        for sv in sv_list:
            sv_list_str += ctx.bot.get_guild(sv).name + f' ({str(sv)})'
            if not c == len(sv_list):
                sv_list_str += ', '
            c += 1
        sv_list_str += '```'

        embed=discord.Embed(color=colors.default)
        embed.add_field(name="Lista de Servidores Liberados:", value=sv_list_str, inline=True)
        embed.set_footer(text=f"Total: {len(sv_list)} servidor(es)")
        await ctx.send(embed=embed)


    @commands.command()
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.guild_check)
    async def oc_pmtmanager(self, ctx, user : discord.User):
        '''adiciona um usuário na lista de managers'''
        settings = configs.get()

        embed=discord.Embed(color=colors.default)
        if user.id in settings['manager-list'] or user.id in settings['developer-list']:
            embed.add_field(name="Resultado:", value="```Usuário já é um manager ou developer.```", inline=True)
        else:
            settings['manager-list'].append(user.id)
            configs.save(settings)
            embed.add_field(name="Resultado:", value="```Usuário adicionado na lista de managers.```", inline=True)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.guild_check)
    async def oc_dmtmanager(self, ctx, user : discord.User):
        '''adiciona um usuário na lista de managers'''
        settings = configs.get()

        embed=discord.Embed(color=colors.default)
        if not user.id in settings['manager-list']:
            embed.add_field(name="Resultado:", value="```Usuário não estava na lista.```", inline=True)
        else:
            settings['manager-list'].remove(user.id)
            configs.save(settings)
            embed.add_field(name="Resultado:", value="```Usuário removido da lista de managers.```", inline=True)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.guild_check)
    async def oc_listmanager(self, ctx):
        '''lista todos os usuários com permissão de manager'''
        settings = configs.get()

        mn_list = settings['manager-list']
        mn_list_str = ''
        c = 1
        for mn in mn_list:
            mn_list_str += ctx.bot.get_user(mn).mention
            if not c == len(mn_list):
                mn_list_str += ', '
            c += 1

        embed=discord.Embed(color=colors.default)
        embed.add_field(name="Lista de Managers:", value=mn_list_str, inline=True)
        embed.set_footer(text=f"Total: {len(mn_list)} manager(s)")
        await ctx.send(embed=embed)


    @commands.command()
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.guild_check)
    async def oc_pmtdeveloper(self, ctx, user : discord.User):
        '''adiciona um usuário na lista de managers'''
        settings = configs.get()

        embed=discord.Embed(color=colors.default)
        if user.id in settings['developer-list']:
            embed.add_field(name="Resultado:", value="```Usuário já é um developer.```", inline=True)
        else:
            settings['developer-list'].append(user.id)
            configs.save(settings)
            embed.add_field(name="Resultado:", value="```Usuário adicionado na lista de developers.```", inline=True)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.guild_check)
    async def oc_dmtdeveloper(self, ctx, user : discord.User):
        '''adiciona um usuário na lista de managers'''
        settings = configs.get()

        embed=discord.Embed(color=colors.default)
        if not user.id in settings['developer-list']:
            embed.add_field(name="Resultado:", value="```Usuário não estava na lista.```", inline=True)
        else:
            settings['developer-list'].remove(user.id)
            configs.save(settings)
            embed.add_field(name="Resultado:", value="```Usuário removido da lista de developers.```", inline=True)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.guild_check)
    async def oc_listdeveloper(self, ctx):
        '''lista todos os usuários com permissão de manager'''
        settings = configs.get()

        dev_list = settings['developer-list']
        dev_list_str = ''
        c = 1
        for dev in dev_list:
            dev_list_str += ctx.bot.get_user(dev).mention
            if not c == len(dev_list):
                dev_list_str += ', '
            c += 1

        embed=discord.Embed(color=colors.default)
        embed.add_field(name="Lista de Developers:", value=dev_list_str, inline=True)
        embed.set_footer(text=f"Total: {len(dev_list)} developer(s)")
        await ctx.send(embed=embed)


    @commands.command()
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.guild_check)
    async def oc_devmode(self, ctx, toggle : str):
        '''ativa ou desativa o modo de desenvolvimento'''
        settings = configs.get()

        embed=discord.Embed(color=colors.default)
        if toggle == 'on':
            settings['development-mode'] = True
            embed.add_field(name="Modo de Desenvolvedor:", value="```🟢Ativado```", inline=True)
            settings['development-mode'] = False
            embed.add_field(name="Modo de Desenvolvedor:", value="```🔴Desativado```", inline=True)
        else:
            raise errors.DevModeUnknown
        configs.save(settings)
        await ctx.send(embed=embed)


    @oc_devmode.error
    async def oc_devmode_error(self, ctx, error):
        if isinstance(error, errors.DevModeUnknown):
            lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
            embed = errors.get_error_embed(lang, 'Modo Desconhecido', tip='Modos conhecidos: on, off')
        else:
            return None
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Developer(bot))