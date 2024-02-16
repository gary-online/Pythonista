import asyncio

async def main():
    print("Hello")
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()