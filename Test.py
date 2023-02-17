import os
import dotenv
import discord

dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")


client = discord.Client()