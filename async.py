import asyncio


a = []

c = ["abc","def", "ghi", "jkl"]


def synchronous_function():
    print(a)
# function that run for see the dict
async def task1():
    print('Task 1 started')
    x = len(a)
    while x < 4:
        synchronous_function()
        x = len(a)
        await asyncio.sleep(1)
    print('Task 1 finished')
# function for add value to dict
async def task2():
    print('Task 2 started')
    for i in c:
        a.append(i)
        print(f"{i} added")
        await asyncio.sleep(1)
    print('Task 2 finished')

async def main():
    # Menjalankan task1 dan task2 secara simultan
    await asyncio.gather(task1(), task2())

# Menjalankan program utama
if __name__ == '__main__':
    asyncio.run(main())
