import discord
from discord.ext import commands


class BaseView(discord.ui.View):
    def __init__(self, *, ctx: commands.Context, timeout: float = 180):
        self.ctx         = ctx
        super().__init__(timeout=timeout)
