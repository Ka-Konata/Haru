import json
from scripts import errors


developer     = 6
manager       = 5
owner         = 4
administrator = 3
moderator     = 2
member        = 1


def get():
    with open('scripts/configs.json') as f:
        configs = json.load(f)
        f.close()
    return configs


def save(actualized_configs):
    obj = json.dumps(actualized_configs, indent=4)
    with open('scripts/configs.json', 'w') as f:
        f.write(obj)
        f.close()


def guild_check(ctx):
    settings = get()
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
