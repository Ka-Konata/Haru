import json, logging
from logging.config import dictConfig
from scripts import errors

developer     = 6
manager       = 5
owner         = 4
administrator = 3
moderator     = 2
member        = 1

LOGGER = {
    "version": 1, 
    "disabled_existing_loggers": False, 
    "formatters":{
        "verbose":{
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard":{
            "format": "%(levelname)-10s - %(name)-15s : %(message)s"
        }
    }, 
    "handlers":{
        "console": {
            'level': "DEBUG", 
            'class': "logging.StreamHandler",
            'formatter': "standard"
        }, 
        "console2": {
            'level': "WARNING", 
            'class': "logging.StreamHandler",
            'formatter': "standard"
        }, 
        "file": {
            'level': "INFO", 
            'class': "logging.FileHandler",
            'filename': "logs/infos.log",
            'mode': "w", 
            'formatter': "verbose"
        }, 
    }, 
    "loggers":{
        "bot": {
            'handlers': ['console'],
            "level": "INFO", 
            "propagate": False
        }, 
        "discord": {
            'handlers': ['console2', "file"],
            "level": "INFO", 
            "propagate": False
        }
    }
}

dictConfig(LOGGER)


def json_open(path):
    with open(path, encoding='utf8') as f:
        cmds = json.load(f)
        f.close()
    return cmds


def get_commands():
    return json_open('storage/commands.json')


def get_guild(guild_id : str):
    guild_id = str(guild_id)
    guilds = json_open('storage/guilds.json')
    try:
        res = guilds[guild_id]
    except Exception as error:
        guilds.update({guild_id:{'prefix':'!h', 'language':'pt-br', 'lockedcommands':[]}})
        res              = guilds[guild_id]
        obj = json.dumps(guilds, indent=4)
        with open('storage/guilds.json', 'w') as f:
            f.write(obj)
            f.close()
    return res



def get_lang(language):
    return json_open(f'storage/languages/{language}.json')


lang = {'pt-br':get_lang('pt-br'), 'en':get_lang('en')}


def get():
    return json_open('storage/configs.json')


def save(actualized_configs):
    obj = json.dumps(actualized_configs, indent=4)
    with open('storage/configs.json', 'w') as f:
        f.write(obj)
        f.close()


def guild_check(ctx):
    settings = get()
    if settings['development-mode'] == False:
        return True
    if not ctx.guild.id in settings['server-list']:
        raise errors.GuildNotAllowed
    return True


def check(ctx, lvl):
    settings = get()
    actual_lvl = 0
    if ctx.author.id in settings['developer-list']:
        actual_lvl = developer
    elif ctx.author.id in settings['manager-list']:
        actual_lvl = manager
    elif ctx.author.id == ctx.guild.owner_id:
        actual_lvl = owner
    elif ctx.author.guild_permissions.administrator:
        actual_lvl = administrator
    elif ctx.author.guild_permissions.ban_members:
        actual_lvl = moderator
    else:
        actual_lvl = member

    if not actual_lvl >= lvl:
        raise errors.AuthenticationFailure


class Authentication:
    def developer(ctx):
        check(ctx, developer)
        return True


    def manager(ctx):
        check(ctx, manager)
        return True


    def owner(ctx):
        check(ctx, owner)
        return True


    def administrator(ctx):
        check(ctx, administrator)
        return True


    def moderator(ctx):
        check(ctx, moderator)
        return True


    def member(ctx):
        check(ctx, member)
        return True
