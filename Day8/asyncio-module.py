import asyncio


async def print_name(fname: str, lname: str):
    flag = True
    # to create an async behaviour we create tasks
    # task = asyncio.create_task(print_middle_name("Sagar"))
    asyncio.ensure_future(print_middle_name("Sagar"))
    print(fname)
    # can await an async function using the await keyword
    # mname = await (print_middle_name("Sagar"))
    # print(mname)
    # mname=await task
    # print(mname)
    print(lname)
    # can await a task at the end so all the synchronous non-blocking code is run first
    if flag:
        return "hello"
    # await task


async def print_middle_name(mname: str):
    await asyncio.sleep(10)
    print(mname)


# asyncio.run(print_name("Kumar", "Maiti"))
loop = asyncio.get_event_loop()
loop.run_until_complete(print_name("Kumar", "Maiti"))
