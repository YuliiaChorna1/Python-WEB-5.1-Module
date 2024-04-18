# Тут ми імітуємо запити до бази даних за допомогою функції get_user_sync 
# і в циклі запитуємо фейкових користувачів з id від 1 до 3. 
# B py_02.py Hа це у нас йде приблизно 1.5 секунди. 
# Прискоримо цей процес за допомогою async/await:

# Ми отримуємо той самий результат, але втричі швидший. 
# Фактично ми запустили три функції get_user_async на паралельне виконання 
# і цей процес зайняв близько 0.5 секунд. Допоміжна функція asyncio.gather потрібна, 
# щоб покласти в чергу кілька співпрограм та дозволити Event loop виконувати їх 
# у будь-якому порядку. Крім того, asyncio.gather повертає 
# результат виконання coroutine у тому порядку, в якому вони були викликані.

import asyncio
from time import time

fake_users = [
    {"id": 1, "name": "April Murphy", "company": "Baily Inc", 
     "email": "shawnlittle@example.org"},
    {"id": 2, "name": "Emily Alexander", "company": "Martinez-Smith", 
     "email": "turnerandrew@example.org"},
    {"id": 3, "name": "Patrick Jones", "company": "Young, Pruitt and Miller", 
     "email": "alancoleman@example.net"}
]

async def get_user_sync(uid: int) -> dict:
    await asyncio.sleep(0.5) # впливає на час виконання всієї програми
    user, = list(filter(lambda user: user["id"] == uid, fake_users)) 
    # "user, = " присвоює значення з ліста, розпаковує ліст
    # ex.: 
    # a, = [1] поверне a = 1 а не ліст
    return user

async def main():
    r = []
    for i in range(1, 4):
        r.append(get_user_sync(i))
    return await asyncio.gather(*r)

if __name__ == '__main__':
    start = time()
    result = asyncio.run(main())
    for r in result:
        print(r)
    print(time() - start)
