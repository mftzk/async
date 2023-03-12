import asyncio


async def do_something():
    await asyncio.sleep(1)
    print("do something")
    
loop = asyncio.get_event_loop()
loop.run_until_complete(do_something())
loop.close()

async def do_something():
    await asyncio.sleep(1)
    print("do something")
    
async def do_another_thing():
    await asyncio.sleep(2)
    print("do another thing")
    
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(do_something(), do_another_thing()))
loop.close()
