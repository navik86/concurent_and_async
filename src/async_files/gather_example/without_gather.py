import asyncio
import time


async def fun1(x):
    print(x**2)
    await asyncio.sleep(3)
    print('fun1 завершена')


async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')


async def main(*args):
    a, b = args
    task1 = asyncio.create_task(fun1(a))
    task2 = asyncio.create_task(fun2(b))

    await task1
    await task2


if __name__ == "__maint__":

    start_time = time.time()
    asyncio.run(main(3, 4))
    end_time = time.time() - start_time
    print(f"\nTime without gather: {end_time} seconds")