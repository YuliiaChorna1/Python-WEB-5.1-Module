# Це найпростіший приклад на async/await. 
# Виклик print(r) нам повертає об'єкт coroutine. 
# Щоб отримати результат від асинхронної функції baz, нам потрібен await. 
# І тільки виконавши result = await r, ми отримаємо у змінній result значення Hello world.

import asyncio

async def baz() -> str:
    print("Before sleep")
    await asyncio.sleep(1)
    print("After Sleep")
    return "Hello world"

async def main():
    r = baz()
    print(r)
    result = await r
    print(result)

if __name__ == '__main__':
    asyncio.run(main())
