import discord
import os
from neuralintents import GenericAssistant



chatbot=GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()
client=discord.Client(intents=discord.Intents.default())
@client.event
async def on_message(message):
    if message.author==client.user:
        return

    if message.content.startswith("$aibot"):
        response=chatbot.request(message.content[7:])
        await message.channel.send(response)




client.run("MTA1MzU0NjAwODYzOTk3NTUwNA.GNi3B6.hgNQO8Vt6TtzjsFMbNZZMc3sJ-zQjlV4q626zs")

