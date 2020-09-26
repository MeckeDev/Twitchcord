import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("DB_HOST")
USER = os.getenv("DB_USER")
PASS = os.getenv("DB_PASS")
NAME = os.getenv("DB_NAME")

db = mysql.connector.connect(
    host = HOST,
    user = USER,
    passwd = PASS,
    db = NAME
)

cur = db.cursor()
cur.execute("SELECT * FROM Artikel")

for row in cur.fetchall():
    print(row[1])

db.close()