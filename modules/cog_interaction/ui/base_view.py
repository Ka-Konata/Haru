import discord
from modules.cog_interaction.ui import generate_embed
from scripts import colors


class CTX():
    def __init__(self, user) -> None:
        self.user = user


class BaseView(discord.ui.View):
    def __init__(self, *, type: str, lang: dict, settings: dict, user1, user2, timeout: float = 180):
        self.type     = type
        self.lang     = lang
        self.settings = settings
        self.user1    = user2 # inverted
        self.user2    = user1 # inverted
        super().__init__(timeout=timeout)


    async def on_timeout(self) -> None:
        for btn in self.children:
            btn.disabled = True
        await self.message.edit(embed=self.message.embeds[0], view=self)    


    async def send_new(self, interaction: discord.Interaction = None):
        gen = generate_embed.generate(self.type, self.lang, self.settings, self.user1, self.user2)
        if interaction.user.id == self.user1.id:
            for btn in self.children:
                btn.disabled = True
            await self.message.edit(embed=self.message.embeds[0], view=self)  
            await interaction.response.send_message(gen['title'], embed=gen['embed'])
        else:
            embed = discord.Embed(description=interaction.user.mention + ', ' + self.lang['COMMAND']['KISS']['WRONG'], color=colors.error)
            await interaction.response.send_message(embed=embed, delete_after=3.5, ephemeral=True)


    @discord.ui.button(label='Retribuir', style=discord.ButtonStyle.gray)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_new(interaction)
