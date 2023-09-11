import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "1464463")

API_HASH = os.environ.get("API_HASH", "ff8451462d91861a13ffd8a6bb72aa8b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6561330005:AAE2Cw0mXmdc_RJtMEyVkF5akWBuRfDbJR0") 

FORCE_SUB = os.environ.get("FORCE_SUB", "animefiles") 

DB_NAME = os.environ.get("DB_NAME","activ3")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://ankit29:ankit29@cluster0.7gdbq.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "100"))

START_PIC = os.environ.get("START_PIC", "https://m.facebook.com/photo.php/?photo_id=441653241329237")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get("ADMIN", '689061386').split()]

PORT = os.environ.get("PORT", "8080")
