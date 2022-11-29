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
    results = asyncio.gather(fun1(a), fun2(b))
    await results


if __name__ == "__maint__":

    start_time = time.time()
    asyncio.run(main(5, 7))
    end_time = time.time() - start_time
    print(f"\nTime with gather: {end_time} seconds")