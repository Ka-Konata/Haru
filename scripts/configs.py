import json, os, pathlib, logging
from logging.config import dictConfig
from scripts import errors

ROOT_DIR = pathlib.Path(__file__).parent.parent
COGS     = list()
COGS.append(ROOT_DIR / 'modules/cog_developer')
COGS.append(ROOT_DIR / 'modules/cog_bot')
COGS.append(ROOT_DIR / 'modules/cog_configuration')
COGS.append(ROOT_DIR / 'modules/cog_utility')
COGS.append(ROOT_DIR / 'modules/cog_fun')
COGS.append(ROOT_DIR / 'modules/cog_minigame')
COGS.append(ROOT_DIR / 'modules/cog_interaction')

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

if not os.path.exists('logs'):
    os.mkdir('logs')
    print('DIRECTORY "LOGS" CREATED')
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


def get_perms_as_dict(aux):
    perms = dict()

    perms['add_reactions'] = aux.add_reactions
    perms['administrator'] = aux.administrator
    perms['attach_files'] = aux.attach_files
    perms['ban_members'] = aux.ban_members
    perms['change_nickname'] = aux.change_nickname
    perms['connect'] = aux.connect
    perms['create_instant_invite'] = aux.create_instant_invite
    perms['create_private_threads'] = aux.create_private_threads
    perms['create_public_threads'] = aux.create_public_threads
    perms['deafen_members'] = aux.deafen_members
    perms['embed_links'] = aux.embed_links
    perms['external_emojis'] = aux.external_emojis
    perms['external_stickers'] = aux.external_stickers
    perms['kick_members'] = aux.kick_members
    perms['manage_channels'] = aux.manage_channels
    perms['manage_emojis'] = aux.manage_emojis
    perms['manage_emojis_and_stickers'] = aux.manage_emojis_and_stickers
    perms['manage_events'] = aux.manage_events
    perms['manage_guild'] = aux.manage_guild
    perms['manage_messages'] = aux.manage_messages
    perms['manage_nicknames'] = aux.manage_nicknames
    perms['manage_permissions'] = aux.manage_permissions
    perms['manage_roles'] = aux.manage_roles
    perms['manage_threads'] = aux.manage_threads
    perms['manage_webhooks'] = aux.manage_webhooks
    perms['mention_everyone'] = aux.mention_everyone
    perms['moderate_members'] = aux.moderate_members
    perms['move_members'] = aux.move_members
    perms['mute_members'] = aux.mute_members
    perms['priority_speaker'] = aux.priority_speaker
    perms['read_message_history'] = aux.read_message_history
    perms['read_messages'] = aux.read_messages
    perms['request_to_speak'] = aux.request_to_speak
    perms['send_messages'] = aux.send_messages
    perms['send_messages_in_threads'] = aux.send_messages_in_threads
    perms['send_tts_messages'] = aux.send_tts_messages
    perms['speak'] = aux.speak
    perms['stream'] = aux.stream
    perms['use_application_commands'] = aux.use_application_commands
    perms['use_embedded_activities'] = aux.use_embedded_activities
    perms['use_external_emojis'] = aux.use_external_emojis
    perms['use_external_stickers'] = aux.use_external_stickers
    perms['use_voice_activation'] = aux.use_voice_activation
    perms['value'] = aux.value
    perms['view_audit_log'] = aux.view_audit_log
    perms['view_channel'] = aux.view_channel
    perms['view_guild_insights'] = aux.view_guild_insights

    return perms
