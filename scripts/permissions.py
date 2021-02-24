import discord

def perms_dict(perms, lang):
    perms_d = {
        "add_reactions":            perms.add_reactions,
        "administrator":            perms.administrator,
        "attach_files":             perms.attach_files,
        "ban_members":              perms.ban_members,
        "change_nickname":          perms.change_nickname,
        "connect":                  perms.connect,
        "create_instant_invite":    perms.create_instant_invite,
        "deafen_members":           perms.deafen_members,
        "embed_links":              perms.embed_links,
        "external_emojis":          perms.external_emojis,
        "kick_members":             perms.kick_members,
        "manage_channels":          perms.manage_channels,
        "manage_emojis":            perms.manage_emojis,
        "manage_guild":             perms.manage_guild,
        "manage_messages":          perms.manage_messages,
        "manage_nicknames":         perms.manage_nicknames,
        "manage_permissions":       perms.manage_permissions,
        "manage_roles":             perms.manage_roles,
        "manage_webhooks":          perms.manage_webhooks,
        "mention_everyone":         perms.mention_everyone,
        "move_members":             perms.move_members,
        "mute_members":             perms.mute_members,
        "priority_speaker":         perms.priority_speaker,
        "read_message_history":     perms.read_message_history,
        "read_messages":            perms.read_messages,
        "send_messages":            perms.send_messages,
        "send_tts_messages":        perms.send_tts_messages,
        "speak":                    perms.speak,
        "stream":                   perms.stream,
        "use_external_emojis":      perms.use_external_emojis,
        #"use_slash_commands":       perms.use_slash_commands,
        "use_voice_activation":     perms.use_voice_activation,
        "value":                    perms.value,
        "view_audit_log":           perms.view_audit_log,
        "view_channel":             perms.view_channel,
        #"view_guild_insights":      perms.view_guild_insights
    }

    retorno = "```"
    n       = 0
    for key in perms_d.keys():
        n  += 1
        if perms_d[key]:
            retorno += lang[key]
        if n < len(perms_d.keys()):
            retorno += ", "
    retorno += "```"

    return retorno

def embed(member, role, perms, lang, colors, message):
    perms_r = perms_dict(perms, lang)

    if member != None:
        desc = lang["PERMS_DESC_MEMBER"]
        ment = member
    elif role != None:
        desc = lang["PERMS_DESC_ROLE"]
        ment = role

    embed = discord.Embed(description=desc + ment.mention, color=colors.Thistle)
    embed.set_author(name=message.author, icon_url=message.author.avatar_url)
    embed.add_field(name=lang["PERMS_FIELD_NAME"], value=perms_r)

    return embed
