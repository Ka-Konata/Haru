import discord, typing, myanimelist
from discord import app_commands
from discord.ext import commands
from scripts import configs
from decouple import config as getenv
from modules.cog_utility.ui_mal import mal_pagination_view
from modules.cog_utility.category_mal import user as mal_user
from modules.cog_utility.category_mal import animelist as mal_animelist
from modules.cog_utility.category_mal import mangalist as mal_mangalist
from math import ceil


class Cmd:
    async def manga(parent, ctx, manga: str):
        pass