# Speed test "with open" vs. "async with async_open"

import asyncio
from time import time
from aiofile import AIOFile, LineReader, async_open

# creating files

async def main(idx):
    async with async_open(f"A_test_{idx}.txt", "w+") as afp:
        await afp.write("Hello ")
        await afp.write("world\n")
        await afp.write("Hello from - Async world!")

def main_sync(idx):
    with open (f"S_test_{idx}.txt", "w+") as fh:
        fh.write("Hello ")
        fh.write("world\n")
        fh.write("Hello from - Sync world!")

# reading files
# ...



if __name__ == '__main__':
    start1 = time()
    for i in range(10):
        asyncio.run(main(i))
    print(f"Async execution time is: {time() - start1}")

    start2 = time()
    for j in range(10):
        main_sync(j)
    print(f"Sync execution time is: {time() - start2}")


