import discord
from transformers import pipeline
token = 'paste your token here that is genrated on discord developmet porttral'

# Load distilGPT-2 pipeline
generator = pipeline('text-generation', model='distilgpt2')

#here i had used simple lightest model only for testing you can user and model as you hardware 
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        prompt = message.content
        response = generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
        await message.channel.send(response)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)
