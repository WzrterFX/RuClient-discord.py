#Библиотеки
import discord
from discord.ext import commands
import requests

#Класс
class injector(commands.Cog):
    def __init__(self, client):
        self.client = client

    #nsfw waifu
    @commands.command()
    @commands.is_nsfw()
    async def waifu(self, ctx):

        req = requests.get("https://api.waifu.pics/nsfw/waifu")    #Делаем запрос
        res = req.json()

        nsfw_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240))
        nsfw_embed.set_image(url=res["url"])

        await ctx.reply(embed=nsfw_embed)

        print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} использовал <waifu> {self}")     #Отчет в консоль

        pass

    #nsfw neko
    @commands.command()
    @commands.is_nsfw()
    async def neko(self, ctx):

        req = requests.get("https://api.waifu.pics/nsfw/neko")    #Делаем запрос
        res = req.json()

        nsfw_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240))
        nsfw_embed.set_image(url=res["url"])

        await ctx.reply(embed=nsfw_embed)

        print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} использовал <neko> {self}")      #Отчет в консоль

        pass

    #nsfw blowjob
    @commands.command()
    @commands.is_nsfw()
    async def blowjob(self, ctx):

        req = requests.get("https://api.waifu.pics/nsfw/blowjob")    #Делаем запрос
        res = req.json()

        nsfw_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240))
        nsfw_embed.set_image(url=res["url"])

        await ctx.reply(embed=nsfw_embed)

        print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} использовал <blowjob> {self}")    #Отчет в консоль

        pass

#Запуск
def setup(client):
    client.add_cog(injector(client))