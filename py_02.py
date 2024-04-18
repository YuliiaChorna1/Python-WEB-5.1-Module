# головна перевага async/await – це прискорення IO запитів. Для демонстрації:
# Тут ми імітуємо запити до бази даних за допомогою функції get_user_sync 
# і в циклі запитуємо фейкових користувачів з id від 1 до 3. 
# На це у нас йде приблизно 1.5 секунди. 
# Прискоримо цей процес за допомогою async/await y py_03.py

from time import sleep, time

fake_users = [
    {"id": 1, "name": "April Murphy", "company": "Baily Inc", 
     "email": "shawnlittle@example.org"},
    {"id": 2, "name": "Emily Alexander", "company": "Martinez-Smith", 
     "email": "turnerandrew@example.org"},
    {"id": 3, "name": "Patrick Jones", "company": "Young, Pruitt and Miller", 
     "email": "alancoleman@example.net"}
]

def get_user_sync(uid: int) -> dict:
    sleep(0.5)
    user, = list(filter(lambda user: user["id"] == uid, fake_users))
    return user

if __name__ == '__main__':
    start = time()
    for i in range(1, 4):
        print(get_user_sync(i))
    print(time() - start)
