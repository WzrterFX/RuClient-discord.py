#Библиотеки
import discord
from discord.ext import commands
import googletrans
from googletrans import Translator

#Класс
class injector(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Переводчик Google
    @commands.command(aliases = ["переведи", "translate", "Translate"])
    async def Переведи(self, ctx, lang, *, text):

        translator = Translator()
        translation = translator.translate(text, dest=lang)

        translator_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240), title = f"<:blurple_verified:1063470348777050163> ┆ Google Переводчик") #Не знал как обыграть пустые символы и оставил так

        translator_embed.add_field(name = f"Исходный текст", value = text, inline = False) #Делаем отделы
        translator_embed.add_field(name = f"Переведенный текст", value = translation.text, inline = False)

        await ctx.reply(embed = translator_embed)
        
        print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} использовал <Переведи> {self}")  #Отчет в консоль

        pass

#Запуск
def setup(client):
    client.add_cog(injector(client))