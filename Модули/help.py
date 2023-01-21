#Библиотеки
import discord
from discord.ext import commands

#Класс
class injector(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("help")	#Удаляем стандартную команду help

    @commands.command(aliases = ["помоги", "help", "Help", "faq", "FAQ", "Faq"])
    async def Помоги(self, ctx):

    	help_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240), title="Все поддерживаемые команды")

    	help_embed.add_field(name="<:blueple_moderation:1065648061004652595> ┆ Модерация", value=f"```r.удалить argument\nr.кикнуть member\nr.забаниить member\nr.разбаниить id```", inline = False)

    	help_embed.add_field(name="<:blueple_user:1065657199394832404> ┆ Пользователь", value=f"```r.переведи lang argument\nr.профиль member\nr.аватар member```", inline = False)

    	help_embed.add_field(name="<:blueple_developer:1065659209875722240> ┆ Разработчик", value=f"```r.рестарт\nr.завершение\nr.cтатус\nr.сервера\nr.пинг\nr.эхо```", inline = False)

    	await ctx.reply(embed = help_embed)

    	pass

#Запуск
def setup(client):
    client.add_cog(injector(client))