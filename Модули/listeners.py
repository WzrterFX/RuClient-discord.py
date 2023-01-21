#Библиотеки
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound, MissingPermissions, MemberNotFound, MissingRequiredArgument

#Класс
class injector(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Реакция на включение
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status = "discord.Status.online", activity = discord.Activity(name = "r.Помоги", type = discord.ActivityType.watching))

        print("\033[91m [КЛИЕНТ] \033[0m" + f"Клиент зарегистрировался как {self.client.user} {self}")  #Отчет в консоль

        pass

    #Реакция на ошибки
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        #Комманда не существует
        if isinstance(error, CommandNotFound):

            command_not_found_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240),
             description = "<:blueple_info:1063513754857373776> ┆ Комманда не найденна") #Делаем плажку

            await ctx.reply(embed = command_not_found_embed)
            print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} ввел несуществующую команду {self}")  #Отчет в консоль

            pass

        #Нету аргумента
        elif isinstance(error, MissingRequiredArgument):

            missing_required_argument_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240),
             description = "<:blueple_info:1063513754857373776> ┆ Ты не ввёл нужные аргументы") #Делаем плажку

            await ctx.reply(embed = missing_required_argument_embed)
            print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} не ввел аргументы {self}")  #Отчет в консоль

            pass

        #Нету прав
        elif isinstance(error, MissingPermissions):

            missing_permissions_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240),
             description = "<:blueple_info:1063513754857373776> ┆ У тебя не достаточно прав для этого действия") #Делаем плажку 

            await ctx.reply(embed = missing_permissions_embed)
            print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} не смог из-за отсуствие прав {self}")  #Отчет в консоль

            pass

        #Участник не найден
        elif isinstance(error, MemberNotFound):

            member_not_found_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240),
             description = "<:blueple_info:1063513754857373776> ┆ Участник не найден") #Делаем плажку 

            await ctx.reply(embed = member_not_found_embed)
            print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} ввел не существующего пользователя {self}")  #Отчет в консоль
            
            pass

        #Если все ок
        else:
            
            pass

#Запуск
def setup(client):
    client.add_cog(injector(client))