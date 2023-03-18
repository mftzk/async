import asyncio
import time

def get_sleep():
    time.sleep(1)
    print("sleep 1")

async def ip_refresh():
        n = 5
        while n >= 0:
            await asyncio.sleep(3)
            print("sleepp")
            print(n)
            n -= 1

async def ip_refresh_2():
        while True:
            await asyncio.sleep(1)
            print("sleepp - 2")
async def main():
    # Menjalankan task1 dan task2 secara simultan
    await asyncio.gather(ip_refresh(), ip_refresh_2())

# Menjalankan program utama
if __name__ == '__main__':
    asyncio.run(main())


