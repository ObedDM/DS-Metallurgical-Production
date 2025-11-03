import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

SILVER_PRODUCTION_URL = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/660/es/00/false/BIE/2.0/{TOKEN}?type=json"