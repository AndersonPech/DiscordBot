import discord
import logging
import datetime

'''
Wish someone a happy birthday via discord
'''

#MTA3ODY3MTQ0NDE3NjgwNTk1OA.GjjA55.gDgzSqCTVOnrtW077ymuOdlklY7hOjB02OhxBk

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')


'''
Read information from google sheets
'''
def ReadSheets():
    pass


'''
If there is someone with a bday today, wish them Hbday otherwise sleep for 24 hours
'''
def BirthdayCheck():
    pass



'''
Discord client
'''
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('my token goes here', log_handler=handler, log_level=logging.DEBUG)

