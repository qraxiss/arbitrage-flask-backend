from dotenv import load_dotenv
import os

load_dotenv()

FEE = 1000000

MONGODB_URI = os.getenv('MONGODB_URI')
DATABASE = os.getenv('DATABASE')
PORT = os.getenv('PORT')
HOST = os.getenv('HOST')
PROTOCOL = os.getenv('PROTOCOL')

from json import load

providers = load(open('config.json', 'r'))