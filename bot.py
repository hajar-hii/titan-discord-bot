import discord
import os
from neuralintents import GenericAssistant
from dotenv import load_dotenv



chatbot=GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()
load_dotenv()

client=discord.Client(intents=discord.Intents.default())
@client.event
async def on_message(message):
    if message.author==client.user:
        return

    if message.content.startswith("$aibot"):
        response=chatbot.request(message.content[7:])
        await message.channel.send(response)




client.run(os.getenv('TOKEN'))

