import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('MTEyNjU5MTMwNTc3MDg4MTE2NQ.Gdq4DO.vxZbljyY8rJo_CvIQ0PR1KVMa--T-Z-IJH2_Qo')