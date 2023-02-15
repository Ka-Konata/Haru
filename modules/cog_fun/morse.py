import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, colors


modulos = configs.get_commands()
morse_dictionary = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "á": ".-",
    "à": ".-",
    "ã": ".-",
    "â": ".-",
    "ä": ".-",
    "é": ".",
    "è": ".",
    "ê": ".",
    "ë": ".",
    "í": "..",
    "ì": "..",
    "î": "..",
    "ï": "..",
    "ó": "---",
    "ò": "---",
    "õ": "---",
    "ô": "---",
    "ö": "---",
    "ú": "..-",
    "ù": "..-",
    "û": "..-",
    "ü": "..-",
    "ç": "-.-.",
    "ñ": "-."
}


class Morse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(aliases=modulos['fun']['morse'])
    @app_commands.describe(
        text='The text you want me to convert',
        translate='Are you trying to translate morse to alphabet?')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def morse(self, ctx, translate: bool, text: str):
        '''Convert a text to morse code or translate from morse code'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        if ctx.interaction == None:
            txt = ctx.message.content.split()[2:]
            text  = ''
            for a in txt:
                text += ' ' + a

        if not translate:
            converted = ''
            invalids  = ''
            for letter in text[0:].lower():
                try:
                    converted += '{} '.format(morse_dictionary[letter])
                except KeyError:
                    if letter != ' ':
                        invalids += f'{letter} '
 
        else:
            converted = ''
            invalids  = ''
            listed = text.split()
            for letter in listed:
                try:
                    converted += '{} '.format(next(key for key, value_ in morse_dictionary.items() if value_ == letter))
                except (KeyError, RuntimeError, StopIteration):
                    invalids += f'{letter} '

        embed = discord.Embed(title=lang['COMMAND']['MORSE']['INVALIDS'] + f'\n``` {invalids} ```', description=lang['COMMAND']['MORSE']['DESC 1']+f' \n```{text}```\n'+lang['COMMAND']['MORSE']['DESC 2']+f' \n``` {converted + " "}```', color=colors.default)
        embed.set_author(name=lang['COMMAND']['MORSE']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['MORSE']['FOOTER'])

        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Morse(bot))
