import asyncio

async def main():
    print('beforeSleep')
    await asyncio.sleep(1)
    print('afterSleep')
    
asyncio.run(main())
## in jupyter notebook you must do this do run async function