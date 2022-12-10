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


def get_guild(guild_id : str, all=False):
    guild_id = str(guild_id)
    guilds = json_open('storage/guilds.json')
    try:
        res = guilds[guild_id] if not all else guilds
    except Exception as error:
        settings = get_configs()
        guilds.update({guild_id:{'prefix':settings['default-prefix'], 'language':settings['default-language'], "lockedcommands": []}})
        res              = guilds[guild_id] if not all else guilds
        obj = json.dumps(guilds, indent=4)
        with open('storage/guilds.json', 'w') as f:
            f.write(obj)
            f.close()
    return res



def get_language(language):
    return json_open(f'storage/languages/{language}.json')


lang = {'pt-br':get_language('pt-br'), 'en':get_language('en')}


def get_configs():
    return json_open('storage/configs.json')


def save(actualized_configs, path='storage/configs.json'):
    obj = json.dumps(actualized_configs, indent=4)
    with open(path, 'w') as f:
        f.write(obj)
        f.close()


def check_islocked(ctx):
    local_locks_cmd  = get_guild(ctx.guild.id)['lockedcommands']
    global_locks_cmd = get_configs()['disabled-commands']

    for cmd in local_locks_cmd:
        if cmd == ctx.command.name:
            raise errors.CommandLocked

    for cmd in global_locks_cmd:
        if cmd == ctx.command.name:
            raise errors.CommandDisabled

    return True


def check_guild(ctx):
    settings = get_configs()
    if settings['development-mode'] == False:
        return True
    if not ctx.guild.id in settings['server-list']:
        raise errors.GuildNotAllowed
    return True


def check_role(ctx, lvl):
    settings = get_configs()
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
        check_role(ctx, developer)
        return True


    def manager(ctx):
        check_role(ctx, manager)
        return True


    def owner(ctx):
        check_role(ctx, owner)
        return True


    def administrator(ctx):
        check_role(ctx, administrator)
        return True


    def moderator(ctx):
        check_role(ctx, moderator)
        return True


    def member(ctx):
        check_role(ctx, member)
        return True
