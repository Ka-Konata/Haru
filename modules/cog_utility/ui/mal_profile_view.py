import discord
from discord.ext import commands


class ProfileView(discord.ui.View):
    def __init__(self, *, ctx: commands.Context, timeout: float = 180):
        self.ctx         = ctx
        self.embeds      = []
        self.page_actual = 0
        self.message     = None
        super().__init__(timeout=timeout)


    async def on_timeout(self) -> None:
        for btn in self.children:
            btn.disabled = True
        await self.message.edit(embed=self.create_list(), view=self)    
        
        
    async def actualize_embed(self, interaction: discord.Interaction = None):
        self.disable_or_enable_buttons()
        await interaction.response.edit_message(embed=self.embeds[self.page_actual], view=self)


    def disable_or_enable_buttons(self):
        btn_previous = self.children[0]
        btn_next     = self.children[1]
        if self.page_actual == 0:  # First Page
            btn_next.disabled = False
            btn_previous.disabled = True
        else:  # Last Page
            btn_next.disabled = True
            btn_previous.disabled = False


    @discord.ui.button(label='◀️', style=discord.ButtonStyle.gray)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.page_actual = 0
        await self.actualize_embed(interaction)


    @discord.ui.button(label='▶️', style=discord.ButtonStyle.gray)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.page_actual = 1
        await self.actualize_embed(interaction)
