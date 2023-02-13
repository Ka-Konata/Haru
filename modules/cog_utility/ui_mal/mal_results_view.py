import discord
from discord.ext import commands


class Select(discord.ui.Select):
    def __init__(self, options: list, _callback: dict, placeholder: str):
        super().__init__(placeholder=placeholder, max_values=1, min_values=1, options=options)
        self.callback_embeds = _callback

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(embed=self.callback_embeds[self.values[0]]) 


class SelectView(discord.ui.View):
    def __init__(self, ctx, SelectMenu: Select, timeout: int = 180):
        super().__init__(timeout=timeout)
        self.add_item(SelectMenu)
