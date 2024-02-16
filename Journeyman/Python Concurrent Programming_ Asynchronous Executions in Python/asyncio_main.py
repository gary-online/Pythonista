import time
import asyncio

async def greetings(message):
    for i in range(6):
        print(message)
        await asyncio.sleep(1)

async def main():
    
    start_time = time.time()
    
    await greetings("Hello")
    await greetings("World")

    end_time = time.time()
    
    print("Control returned to main()")
    print("Total time:", end_time-start_time)
    
asyncio.run(main())