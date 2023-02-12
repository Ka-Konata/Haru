import discord
from discord.ext import commands
from scripts import configs, colors
from math import ceil


class PaginationView(discord.ui.View):
    def __init__(self, *, ctx: commands.Context, timeout: float = 180):
        self.ctx         = ctx
        self.storage     = ''
        self.embeded     = False
        self.user_list   = False
        self.username    = ''
        self.list_type   = ''
        self.pages       = 0
        self.page_actual = 0
        self.interaction = None

        super().__init__(timeout=timeout)


    async def on_timeout(self) -> None:
        for btn in self.children:
            btn.disabled = True
        await self.message.edit(embed=self.create_list(), view=self)


    def create_list(self): 
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(self.ctx.guild.id)['language']]['COMMAND']['MAL USER_ANIME_LIST']
        if self.user_list:
            embed = discord.Embed(description=lang['TITLE 1']+self.username+f'](https://myanimelist.net/profile/{self.username})'+lang['TITLE 2']+f'{self.page_actual+1}/{self.pages} ({len(self.storage)}'+lang['TITLE 3'], color=colors.default)
        else:
            embed = discord.Embed()

        if self.embeded:

            item = self.storage[self.page_actual]
            embed.title = f'{item.title}'
            embed.description = lang['EMBED 1']+f'(https://myanimelist.net/{self.list_type}/{item.id}) | '+lang['EMBED 2']+f'(https://myanimelist.net/profile/{self.username})'
            embed.set_image(url=str(item.image))
            if self.user_list:
                score          = item.list_status.score
                status         = item.list_status.status
                done_ep_or_ch  = item.list_status.num_episodes_watched if self.list_type == 'anime' else item.list_status.num_chapters_read
                total_ep_or_ch = item.num_episodes if self.list_type == 'anime' else item.num_chapters
                volumes_read   = f'`(Vol. {item.list_status.num_volumes_read}/{item.num_volumes if item.num_volumes > 0 else "?"})`' if self.list_type == 'manga' else ''
                
                embed.add_field(name=lang['EMBED']['RANK']+f'{item.rank} ({item.mean})', value=lang['EMBED']['SCORE']+f'`{score}`\n'+lang['EMBED']['STATUS']+lang['EMBED']['STATUS LIST'][status]+f' `{done_ep_or_ch}/{total_ep_or_ch}` {volumes_read}')
            else:
                pass
        else:
            c = self.page_actual*20
            res = ''
            content_list = self.storage[c:(self.page_actual+1)*20] if len(self.storage) > (self.page_actual+1)*20 else self.storage[c:]
            for actual in content_list:

                c += 1
                if self.user_list:
                    if actual.list_status != None:
                        score          = actual.list_status.score
                        status         = actual.list_status.status
                        done_ep_or_ch  = actual.list_status.num_episodes_watched if self.list_type == 'anime' else actual.list_status.num_chapters_read
                        total_ep_or_ch = actual.num_episodes if self.list_type == 'anime' else actual.num_chapters
                        volumes_read   = f'`(Vol. {actual.list_status.num_volumes_read}/{actual.num_volumes if actual.num_volumes > 0 else "?"})`' if self.list_type == 'manga' else ''
                    else:
                        print('Nonetype', actual)

                    embed.add_field(name=f'{c}. {actual.title}', value=lang['LIST']+f'(https://myanimelist.net/{self.list_type}/{actual.id}) \n'+lang['EMBED']['SCORE']+f'`{score}`\n'+lang['EMBED']['STATUS']+lang['EMBED']['STATUS LIST'][status]+f' `{done_ep_or_ch}/{total_ep_or_ch}` {volumes_read}', inline=False)
                else:
                    res = res + f'**{c}.** {actual}\n'
        embed.set_footer(text=lang['FOOTER 1']+f'{self.page_actual+1}/{self.pages} | '+lang['FOOTER 2'])
        return embed


    def disable_or_enable_buttons(self):
        btn_previous = self.children[0]
        btn_next     = self.children[2]
        if self.pages == 1: # There's just one page
            btn_next.disabled = True
            btn_previous.disabled = True
        elif self.page_actual == 0:  # First Page
            btn_next.disabled = False
            btn_previous.disabled = True
        elif self.page_actual == self.pages-1:  # Last Page
            btn_next.disabled = True
            btn_previous.disabled = False
        else:  # Any Middle Page
            btn_next.disabled = False
            btn_previous.disabled = False

    
    async def actualize_embed(self, interaction: discord.Interaction = None):
        anime_list = self.create_list()
        self.disable_or_enable_buttons()
        await interaction.response.edit_message(embed=anime_list, view=self)


    @discord.ui.button(label='◀️', style=discord.ButtonStyle.gray)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.page_actual -= 1
        await self.actualize_embed(interaction)


    @discord.ui.button(label='📖 Change View', style=discord.ButtonStyle.gray)
    async def change_vizualization(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.embeded:
            self.embeded = False
            self.pages = ceil(len(self.storage) / 20)
        else:
            self.embeded = True
            self.pages = len(self.storage)
        self.page_actual = 0
        await self.actualize_embed(interaction)


    @discord.ui.button(label='▶️', style=discord.ButtonStyle.gray)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.page_actual += 1
        await self.actualize_embed(interaction)
