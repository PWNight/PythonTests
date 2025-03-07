import asyncio

async def task(name, delay):
    print(f"Задача {name} началась")
    await asyncio.sleep(delay)
    print(f"Задача {name} завершила работу через {delay} секунд")

async def main():
    tasks = [
        task("a",1),
        task("b", 4),
        task("c", 2),
        task("d", 3),
        task("e", 6),
    ]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())