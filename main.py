import discord, datetime
from discord.ext import commands

from modules.developer import Developer
from scripts import configs, errors
#from modules import aliases, developer
from decouple import config as getenv

settings = configs.get()

TOKEN   = getenv('TOKEN')  # Procura o token nas variáveis de ambiente
intents = discord.Intents.default()
intents.members         = True
intents.message_content = True
bot     = commands.Bot(command_prefix=settings['defaul_prefix'], intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} foi conectada ao discord.')
    settings['started_at'] = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    configs.save(settings)

    await bot.load_extension('modules.developer')
    await bot.tree.sync()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, errors.GuildNotAllowed):
        embed = errors.get_error_embed('Servidor não permitido')

    elif isinstance(error, errors.AuthenticationFailure):
        auth = ctx.command.checks[1].__name__ if len(ctx.command.checks) > 1 else ctx.command.checks[0].__name__
        embed = errors.get_error_embed('Erro de Autênticação', f'Nível de Permissão Requerido: {auth}')

    elif isinstance(error, commands.errors.MemberNotFound):
        embed = errors.get_error_embed('Membro não Encontrado')

    elif isinstance(error, commands.errors.UserNotFound):
        embed = errors.get_error_embed('Usuário não Encontrado')

    elif isinstance(error, commands.errors.GuildNotFound):
        embed = errors.get_error_embed('Servidor não Encontrado')

    elif isinstance(error, commands.errors.MissingRequiredArgument):
        embed = errors.get_error_embed('Campo Obrigatório não Preenchido')
    else:
        embed = errors.get_error_embed(error)

    await ctx.send(embed=embed)


bot.run(TOKEN)
