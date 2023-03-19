import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20777636")

API_HASH = os.environ.get("API_HASH", "5b184795fd3f77557caf195b9ba9ba8c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5905002827:AAGzr_H9zijLKorWxZpIFABXB2RHNtGhj8s") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Cyber_Robots") 

DB_NAME = os.environ.get("DB_NAME","clusters0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://TELEGRAM:TELEGRAM@cluster0.tznsnwb.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/012640db59c99c7f92926.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5935204617').split()]

PORT = os.environ.get('PORT', '8080')

WEBHOOK = bool(os.environ.get("WEBHOOK", True))
