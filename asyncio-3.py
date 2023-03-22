import asyncio

async def coroutine():
    print('Start')
    await asyncio.sleep(1)
    return 'Done'

async def main():
    loop = asyncio.get_event_loop()
    task = loop.create_task(coroutine())
    result = await task
    print(result)

if __name__ == '__main__':
    asyncio.run(main())





