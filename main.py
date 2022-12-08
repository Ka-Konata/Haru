import discord, datetime
from discord.ext import commands

from modules.developer     import Developer
from modules.bot           import Bot
from modules.configuration import Configuration
from modules.utility       import Utility
from modules.fun           import Fun
from modules.interaction   import Interaction

from scripts  import configs, errors
from decouple import config as getenv

settings = configs.get()
logger = configs.logging.getLogger('discord')

if len(settings['server-list']) == 0:
    sv = int(input('Não há nenhum servidor na lista de servidores de teste, insira um.\nID do servidor: '))
    settings['server-list'].append(sv)
if len(settings['developer-list']) == 0:
    dev = int(input('Não há nenhum desenvolvedor na lista, insira um.\nID do usuário: '))
    settings['developer-list'].append(dev)

TOKEN   = getenv('TOKEN')  # Procura o token nas variáveis de ambiente
intents = discord.Intents.default()
intents.members         = True
intents.message_content = True
bot     = commands.Bot(command_prefix=settings['default-prefix'], intents=intents)


@bot.event
async def on_ready():
    settings['started-at'] = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    configs.save(settings)   

    #print(f'{bot.user} foi conectada ao discord.')
    logger.info(f'Haru está online (User: {bot.user}) (ID: {bot.user.id})')

    bot.remove_command('help')
    await bot.load_extension('modules.developer')
    await bot.load_extension('modules.bot')
    await bot.load_extension('modules.configuration')
    await bot.load_extension('modules.utility')
    await bot.load_extension('modules.fun')
    await bot.load_extension('modules.interaction')

    await bot.tree.sync()


@bot.event
async def on_message(message):
    guild = configs.get_guild(message.guild.id)
    guild_prefix = guild['prefix']

    if  guild_prefix in message.content:
        message.content = message.content.replace(guild_prefix, settings['default-prefix'])

    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

    for err in errors.local_errors:
        if isinstance(error, err):
            return None

    if isinstance(error, commands.errors.CommandNotFound):
        embed = errors.get_error_embed(lang, lang['ERROR']['CommandNotFound']['TYPE'])

    elif isinstance(error, errors.GuildNotAllowed):
        embed = errors.get_error_embed(lang, lang['ERROR']['GuildNotAllowed']['TYPE'], lang['ERROR']['GuildNotAllowed']['REASON'])

    elif isinstance(error, errors.AuthenticationFailure):
        auth = ctx.command.checks[1].__name__ if len(ctx.command.checks) > 1 else ctx.command.checks[0].__name__
        embed = errors.get_error_embed(lang, lang['ERROR']['AuthenticationFailure']['TYPE'], lang['ERROR']['AuthenticationFailure']['REASON']+auth)

    elif isinstance(error, commands.errors.MemberNotFound):
        embed = errors.get_error_embed(lang, lang['ERROR']['MemberNotFound']['TYPE'])

    elif isinstance(error, commands.errors.UserNotFound):
        embed = errors.get_error_embed(lang, lang['ERROR']['UserNotFound']['TYPE'])

    elif isinstance(error, commands.errors.GuildNotFound):
        embed = errors.get_error_embed(lang, lang['ERROR']['GuildNotFound']['TYPE'])

    elif isinstance(error, commands.errors.MissingRequiredArgument):
        arg = str(list(ctx.command.clean_params.keys())).replace('[', '').replace(']', '').replace("'", '')
        embed = errors.get_error_embed(lang, lang['ERROR']['MissingRequiredArgument']['TYPE'], tip=lang['ERROR']['MissingRequiredArgument']['REASON']+arg)
    else:
        if settings['development-mode']:
            embed = errors.get_error_embed(lang, error, unknown=True)
            logger.error(f'{error}')
        else:
            return None

    await ctx.send(embed=embed)
    #raise error


bot.run(TOKEN)
