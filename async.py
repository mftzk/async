import asyncio
import time

a = []

async def task1():
    print('Task 1 started')
    await asyncio.sleep(2)
    print(a)
    print('Task 1 finished')

async def task2():
    print('Task 2 started')
    for i in ["abc","def"]:
        a.append(i)

    await asyncio.sleep(1)
    print('Task 2 finished')

async def main():
    # Menjalankan task1 dan task2 secara simultan
    await asyncio.gather(task1(), task2())

# Menjalankan program utama
if __name__ == '__main__':
    asyncio.run(main())
