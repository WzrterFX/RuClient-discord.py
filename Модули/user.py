#Библиотеки
import discord
from discord.ext import commands

#Класс
class injector(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Профиль
    @commands.command(aliases = ["профиль", "profile", "Profile"])
    async def Профиль(self, ctx, user : discord.Member = None):

        if user is None:    #Если нету аргумента, аргумент это отправитель
            user = ctx.author

        ctx_is_bot = "Да" if user.bot else "Нет"    #Проверка на бота

        user_info_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240), title = f"<:blueple_info:1063513754857373776> ┆ Информация о пользователе {user}")

        user_info_embed.add_field(name = "Имя пользователя", value = user)
        user_info_embed.add_field(name = "ID пользователя", value = user.id)
        user_info_embed.add_field(name = "Робот", value = ctx_is_bot)

        user_info_embed.add_field(name = "Дата регистрации", value = user.created_at.strftime("%#d %B %Y, %H:%M"))
        user_info_embed.add_field(name = "Присойденился на сервер", value = user.joined_at.strftime("%#d %B %Y, %H:%M"))

        user_info_embed.set_thumbnail(url = user.avatar_url)

        await ctx.reply(embed = user_info_embed)

        print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} использовал <Профиль> {self}")   #Отчет в консоль

        pass

    #Аватар
    @commands.command(aliases = ["аватар", "avatar", "Avatar", "pfp", "Pfp"])
    async def Аватар(self, ctx, *, member: discord.Member = None):

        if not member:   #Если нету аргумента, аргумент это отправитель
            member = ctx.message.author

        avatar_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240), title = f"<:blueple_info:1063513754857373776> ┆ Аватар {member}")
        avatar_embed.set_image(url= f"{member.avatar_url}")

        await ctx.reply(embed=avatar_embed)

        print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} использовал <Аватар> {self}")    #Отчет в консоль

        pass

#Запуск
def setup(client):
    client.add_cog(injector(client))