#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "33516244"))
API_HASH = environ.get("API_HASH", "c1abd0630fcd54d33bc6528ec0955fff")
BOT_TOKEN = environ.get("BOT_TOKEN", "8003550638:AAHPGUxAXWRT2P0VbCC-7Y2nrR2tlVcH-HQ")

OWNER = int(environ.get("OWNER", "obito"))
CREDIT = environ.get("CREDIT", "obitouchiha")

TOTAL_USER = os.environ.get('TOTAL_USERS', '').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

