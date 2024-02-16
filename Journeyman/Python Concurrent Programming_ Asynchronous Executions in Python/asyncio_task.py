import time
import asyncio

async def greetings(message):
    for i in range(6):
        print(message)
        await asyncio.sleep(1)

async def main():
    
    start_time = time.time()
    
    task_1 = asyncio.create_task(greetings("Hello"))
    task_2 = asyncio.create_task(greetings("World"))
    
    await task_1
    await task_2
  
    end_time = time.time()
    
    print("Control returned to main()")
    print("Total time:", end_time-start_time)
    
asyncio.run(main())