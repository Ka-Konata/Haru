import typing
import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class Developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(aliases=['_stts', '_status'])
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.check_guild)
    async def oc_status(self, ctx):
        '''Envia um hello world, e os status do bot'''
        settings = configs.get_configs()

        embed = discord.Embed(title='', description=f'**User do Bot:** {self.bot.user.mention}\n**ID do bot:** {self.bot.user.id}\n**Iniciado em:** {settings["started-at"]}', color=colors.default)
        embed.set_author(name=settings["bot-name"], icon_url=settings["bot-icon"])
        embed.add_field(name='Status do Bot', value=f'```🟢Online  |  🏓Ping: {round(self.bot.latency * 1000)}ms```', inline=False)
        await ctx.reply(embed=embed, mention_author=False)


    @commands.command(aliases=['_quit'])
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.check_guild)
    async def oc_quit(self, ctx):
        '''Força a parar o bot'''
        settings = configs.get_configs()

        embed=discord.Embed(color=colors.default)
        embed.add_field(name='Status do Bot', value=f'```🔴Offline  |  🏓Ping: {round(self.bot.latency * 1000)}ms```', inline=True)
        await ctx.reply(embed=embed, mention_author=False)
        quit()
 

    @commands.command(aliases=['_setsv'])
    @commands.check(configs.Authentication.manager)
    async def oc_setsv(self, ctx, guild : discord.Guild = None):
        '''Libera o uso do bot no servidor atual'''
        settings = configs.get_configs()

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
        await ctx.reply(embed=embed, mention_author=False)


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


    @commands.command(aliases=['_listsv'])
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.check_guild)
    async def oc_listsv(self, ctx):
        '''Lista todos os servidores liberados'''
        settings = configs.get_configs()

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
        await ctx.reply(embed=embed, mention_author=False)


    @commands.command(aliases=['_pmtmanager'])
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.check_guild)
    async def oc_pmtmanager(self, ctx, user : discord.User):
        '''Adiciona um usuário na lista de managers'''
        settings = configs.get_configs()

        embed=discord.Embed(color=colors.default)
        if user.id in settings['manager-list'] or user.id in settings['developer-list']:
            embed.add_field(name="Resultado:", value="```Usuário já é um manager ou developer.```", inline=True)
        else:
            settings['manager-list'].append(user.id)
            configs.save(settings)
            embed.add_field(name="Resultado:", value="```Usuário adicionado na lista de managers.```", inline=True)
        await ctx.reply(embed=embed, mention_author=False)


    @commands.command(aliases=['_dmtmanager'])
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.check_guild)
    async def oc_dmtmanager(self, ctx, user : discord.User):
        '''Adiciona um usuário na lista de managers'''
        settings = configs.get_configs()

        embed=discord.Embed(color=colors.default)
        if not user.id in settings['manager-list']:
            embed.add_field(name="Resultado:", value="```Usuário não estava na lista.```", inline=True)
        else:
            settings['manager-list'].remove(user.id)
            configs.save(settings)
            embed.add_field(name="Resultado:", value="```Usuário removido da lista de managers.```", inline=True)
        await ctx.reply(embed=embed, mention_author=False)


    @commands.command(aliases=['_listmanager'])
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.check_guild)
    async def oc_listmanager(self, ctx):
        '''Lista todos os usuários com permissão de manager'''
        settings = configs.get_configs()

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
        await ctx.reply(embed=embed, mention_author=False)


    @commands.command(aliases=['_pmtdeveloper'])
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.check_guild)
    async def oc_pmtdeveloper(self, ctx, user : discord.User):
        '''Adiciona um usuário na lista de managers'''
        settings = configs.get_configs()

        embed=discord.Embed(color=colors.default)
        if user.id in settings['developer-list']:
            embed.add_field(name="Resultado:", value="```Usuário já é um developer.```", inline=True)
        else:
            settings['developer-list'].append(user.id)
            configs.save(settings)
            embed.add_field(name="Resultado:", value="```Usuário adicionado na lista de developers.```", inline=True)
        await ctx.reply(embed=embed, mention_author=False)


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


    @commands.command(aliases=['_listdeveloper'])
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.check_guild)
    async def oc_listdeveloper(self, ctx):
        '''Lista todos os usuários com permissão de manager'''
        settings = configs.get_configs()

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
        await ctx.reply(embed=embed, mention_author=False)


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


    @commands.command(aliases=['_errorsmode'])
    @commands.check(configs.Authentication.developer)
    @commands.check(configs.check_guild)
    async def oc_errorsmode(self, ctx, toggle : str):
        '''Ativa ou desativa o modo de debug de erros'''
        settings = configs.get_configs()

        embed=discord.Embed(color=colors.default)
        if toggle == 'on':
            settings['errors-mode'] = True
            embed.add_field(name="Modo de Debug de Erros:", value="```🟢Ativado```", inline=True)
        elif toggle == 'off':
            settings['errors-mode'] = False
            embed.add_field(name="Modo de Debug de Erros:", value="```🔴Desativado```", inline=True)
        else:
            raise errors.DevModeUnknown
        configs.save(settings)
        await ctx.reply(embed=embed, mention_author=False)


    @oc_errorsmode.error
    async def oc_errorsmode_error(self, ctx, error):
        if isinstance(error, errors.DevModeUnknown):
            lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
            embed = errors.get_error_embed(lang, 'Modo Desconhecido', tip='Modos conhecidos: on, off')
        else:
            return None
        await ctx.reply(embed=embed, mention_author=False)


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

    
    @commands.command(aliases=['_botsettings'])
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.check_guild)
    async def oc_botsettings(self, ctx): 
        '''Lista todas as configurações do bot'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        guild = configs.get_guild(ctx.guild.id)

        prefix         = settings['default-prefix']
        language       = settings['default-language']
        devmode        = '🟢On' if settings['development-mode'] else '🔴Off'
        errorsmode     = '🟢On' if settings['errors-mode'] else '🔴Off'
        lockedcommands = ''
        for cmd in settings['disabled-commands']:
            lockedcommands = lockedcommands+'`'+cmd+'`\t'
        if len(settings['disabled-commands']) == 0:
            lockedcommands = '`nenhum`'

        embed = discord.Embed(description='', color=colors.default)
        embed.set_author(name='Informações e Configurações Padrão', icon_url=settings['bot-icon'])
        embed.add_field(name='Informações do Bot:', value=f'**User:** {self.bot.user.mention}\n**ID:** {self.bot.user.id}\n**Iniciado em:** {settings["started-at"]}', inline=True)
        embed.add_field(name='Status do Bot', value=f'```🟢Online\n🏓Ping: {round(self.bot.latency * 1000)}ms```', inline=True)
        embed.add_field(name='Configurações Padrão', value=f'```prefixo: {prefix}\nidioma: {language}```', inline=True)
        embed.add_field(name='Modos Especiais', value=f'```Desenvolvimento: {devmode} \nDebug de Erros: {errorsmode}```', inline=True)
        embed.add_field(name='Comandos Desabilitados Globalmente', value=lockedcommands, inline=True)

        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Developer(bot))
