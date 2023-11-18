import discord, datetime
from discord.ext import commands
from scripts  import configs, errors
from decouple import config as getenv
import keep_alive

settings = configs.get_configs()
logger   = configs.logging.getLogger('discord')


if len(settings['server-list']) == 0:
    logger.error(f'No registered server')
    sv = int(input('Insert your server ID: '))
    settings['server-list'].append(sv)
if len(settings['developer-list']) == 0:
    logger.error(f'No registered developer')
    dev = int(input('Insert your user ID: '))
    settings['developer-list'].append(dev)


TOKEN   = getenv('TOKEN')  # Procura o token nas variáveis de ambiente
intents = discord.Intents.default()
intents.members         = True
intents.message_content = True
bot     = commands.Bot(command_prefix=settings['default-prefix'], intents=intents)


@bot.event
async def on_ready():
    settings['started-at'] = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    settings['bot-id']     = bot.user.id
    configs.save(settings)   

    #print(f'{bot.user} foi conectada ao discord.')
    logger.info(f'Haru is online (User: {bot.user}) (ID: {bot.user.id})')

    bot.remove_command('help')

    for cog_directory in configs.COGS:
        for cog_file in cog_directory.glob('*.py'):
            if cog_file.name != '__init__.py':
                await bot.load_extension(f'modules.{cog_directory.name}.{cog_file.name[:-3]}')
                logger.info(f'Extension loaded (Name: modules.{cog_directory.name}.{cog_file.name[:-3]})')

    await bot.tree.sync()
    logger.info('For now, everything is working well')


@bot.event
async def on_message(message):
    if message.author.id == settings["bot-id"]:
        return None
    guild = configs.get_guild(message.guild.id)
    guild_prefix = guild['prefix']

    if  message.content.startswith(guild_prefix):
        message.content = message.content.replace(guild_prefix, settings['default-prefix'], 1)
    elif message.content.startswith(settings['default-prefix']) and settings['default-prefix'] != guild_prefix:
        return None

    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    settings = configs.get_configs()
    lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
    name = error.__class__.__name__

    for err in errors.local_errors:
        if isinstance(error, err):
            return None
    
    tip_arg = rea_arg = ''
    if isinstance(error, errors.AuthenticationFailure):
        rea_arg = ctx.command.checks[1].__name__ if len(ctx.command.checks) > 1 else ctx.command.checks[0].__name__
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        tip_arg = str(list(ctx.command.clean_params.keys())).replace('[', '').replace(']', '').replace("'", '')

    embed = None
    for err in errors.global_errors:
        if isinstance(error, err):
            type   = lang['ERROR'][name]['TYPE']
            reason = lang['ERROR'][name]['REASON'] if rea_arg == '' else lang['ERROR'][name]['REASON']+rea_arg
            tip    = lang['ERROR'][name]['TIP'] if tip_arg == '' else lang['ERROR'][name]['TIP']+tip_arg
            embed  = errors.get_error_embed(lang, type, reason, tip)

    if embed == None:
        if settings['errors-mode']:
            embed = errors.get_error_embed(lang, error, unknown=True)
            logger.error(f'{error}')
            await ctx.reply(embed=embed, mention_author=False)
            raise error
        else:
            embed = errors.get_error_embed(lang, lang['ERROR']['UnknownError']['TYPE'])
            logger.error(f'{error}')

    await ctx.reply(embed=embed, mention_author=False)

# Creating a Server
keep_alive.keep_alive()

bot.run(TOKEN)
commands.Context