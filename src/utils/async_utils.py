import asyncio

def run_async(async_callback, *data):
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(async_callback(*data))

