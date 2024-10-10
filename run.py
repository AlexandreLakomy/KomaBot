import discord
from discord.ext import commands
from response import handle_response  # Import direct de la fonction
from dotenv import load_dotenv
import os

# Charger les variables d'environnement du fichier .env
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True  # Activer l'intent pour les contenus des messages
KOMA_TOKEN = os.getenv('KOMA_TOKEN')

# Vérification que le token a bien été chargé
if KOMA_TOKEN is None:
    raise ValueError("Le token KOMA_TOKEN n'a pas été trouvé. Vérifie ton fichier .env.")

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} est prêt et en ligne !')

async def send_message(message, user_message, is_private):
    try:
        response = handle_response(user_message)  # Appel direct de la fonction
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said: '{user_message}' ({channel})")

    if user_message[0] == '?':
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)

# Lancement du bot
client.run(KOMA_TOKEN)
