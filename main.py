import discord
import logging
import datetime
import pause
import os
import sheets

'''
Wish someone a happy birthday via discord
'''

token = os.environ.get('token')
channel_id = os.environ.get('channel_id')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
ONE_DAY = 86400


'''
Read information from google sheets
'''
def ReadSheets():
    date = datetime.datetime.today().strftime("%d/%m/%y")
    date_split = date.split('/')
    return sheets.fetch_data(['07', '04', '2023'])


'''
If there is someone with a bday today, wish them Hbday otherwise sleep for 24 hours
'''
async def BirthdayCheck():
    birthday_people = ReadSheets()
    for data in birthday_people:
        channel = client.get_channel(channel_id)
        await channel.send(f'It\'s {data[0]} @{data[2]}  birthday today! Wish them a Happy Birthday!', file=discord.File('images/1.gif'))
    
    t = datetime.datetime.today()
    t = t + datetime.timedelta(days=1)
    future = datetime.datetime(t.year, t.month, t.day, t.hour, t.minute, t.second)
    print(future)
    await pause.until(future)

'''
Discord client
'''
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        while (1):
            await BirthdayCheck()


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)
    client.run(token, log_handler=handler, log_level=logging.DEBUG)

