from dotenv import load_dotenv
import discord
import logging
import datetime
import pause
import os
import sheets

'''
Wish someone a happy birthday via discord
'''
load_dotenv()
token = os.getenv('token')
channel_id = os.getenv('channel_id')
GUILD = os.getenv('GUILD')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
ONE_DAY = 86400
intents = discord.Intents.all()


'''
Read information from google sheets
'''
def ReadSheets():
    date = datetime.datetime.today().strftime("%d/%m/%y")
    date_split = date.split('/')
    return sheets.fetch_data(date_split)


'''
If there is someone with a bday today, wish them Hbday otherwise sleep for 24 hours
'''
async def BirthdayCheck():
    birthday_people = ReadSheets()
    allowed_mentions = discord.AllowedMentions(everyone = True, users=True)
    channel = client.get_channel(int(channel_id))
    guild = client.get_guild(int(GUILD))
    for data in birthday_people:
        member = await guild.query_members(str(data[2][:-5])) #If this line is removed, the next one which is more accurate doesn't work. Not sure why
        member2 = discord.utils.get(client.get_all_members(), name=str(data[2][:-5]), discriminator=str(data[2][-4:]))
        user = ''
        if member2 == None: 
            user = data[0]
        else:
            user = f'<@{member2.id}>'

        await channel.send(f'@everyone It\'s {user}  birthday today! Wish them a Happy Birthday!', file=discord.File('images/1.gif'), allowed_mentions = allowed_mentions)


'''
Discord client
'''
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        while (1):
            await BirthdayCheck()
            t = datetime.datetime.today()
            t = t + datetime.timedelta(minute=1)
            future = datetime.datetime(t.year, t.month, t.day, t.hour, t.minute, t.second)
            print(future)
            pause.until(future)


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)
    client.run(token, log_handler=handler, log_level=logging.DEBUG)

