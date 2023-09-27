# database.py
import asyncio
from aiopg import connect

# Tạo đối tượng Database
async def connect_to_db():
  db = await connect(
    engine = 'django.db.backends.mysql',
    database='bookingweb',
    user='root',
    password='Akm246782',
    host='127.0.0.1',
    port=3306
  )
  return db