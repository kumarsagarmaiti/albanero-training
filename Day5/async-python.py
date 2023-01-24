# The asyncio module. The asyncio module comes with excellent features that allow us to write more efficient Python asynchronous applications.
# An asyncio is a Python library which is used to run the concurrent code using the async/wait. It is a foundation for Python asynchronous framework that offers connection libraries, network and web-servers, database distributed task queues, high-performance, etc. This module provides the framework that works around the event loop and also take care of such things as I/O and system events. As far as OS is concerned you’re going to have one process and there’s going to be a single thread within that process, but you’ll be able to do multiple things at once.

import asyncio


async def main():
    print("Waiting 5 seconds. ")
    for _ in range(5):
        await asyncio.sleep(1)
        print("Hello")
    print("Finished waiting.")
asyncio.run(main())

# asyncio uses different constructs: event loops, coroutines and futures.

# An event loop manages and distributes the execution of different tasks. It registers them and handles distributing the flow of control between them.
# Coroutines (covered above) are special functions that work similarly to Python generators, on await they release the flow of control back to the event loop. A coroutine needs to be scheduled to run on the event loop, once scheduled coroutines are wrapped in Tasks which is a type of Future.
# Futures represent the result of a task that may or may not have been executed. This result may be an exception.

# Manage an async event loop in Python
# Asyncio is also used for managing the async event loop. An event loop is an object that runs async functions and callbacks. When we want to execute the coroutines, the event will be crucial for the asynchronous functions when we run the asyncio.run() method; the event loop object is created automatically. To implement the more advanced server, we will need lower-level access to the event loop. We need to work directly with the event loop's internals.

# The event loop comes with the following features.

# It can register, execute, and cancel delayed calls (asynchronous functions)
# It can create client and server transports for communication
# It can create subprocesses and transports for communication with another program.
# Delegate function calls to a pool of threads.

# Read and Write Data with Stream in Python
# The asyncio module offers stream which is used to perform high-level network I/O. It can behave as a server for network requests. It is best for long-running network operations where application block waiting for some other resources to return a result.

# There are two classes, StreamReader and StreamWriter of asyncio. These classes are used to read and write from the network at a high level.

# To read from network, we need to open the network using the asyncio.open_connection(). The StreamReader and StreamWriter objects function return tuple, we would use .read() and .write() method to each connection.

# The asyncio.start_server() method is used to receive the connection from the remote hosts. This function takes a callback function, client_connected_cb as arguments. It is called whenever the function received the request.

# Synchronization tasks in Python
# We have discussed earlier, Asynchronous program runs separately, but sometimes we would want to communicate with each other. The asyncio module offers us a queue and various other methods to establish the synchronization between the tasks.

# Let's understand the following implementation method.

# Queues - The asyncio queues facilitate asynchronous functions to line up Python objects to be consumed by other async functions. For example - The workload is distributed between the function on its behavior.
# Synchronization Primitive - The asyncio's features locks, events, conditions, and semaphores act as conventional Python counterparts.
# Here, a point should always keep in mind that these methods are not thread-safe. This isn't an issue for async tasks running in the same event loop. But we need to use the thread module to share the information between the tasks.

# When to use asynchronous programming?
# In the following scenario, we can use asynchronous programming.

# When we want complete work in quick time.
# The delay involves waiting for I/O (disk or network) operations, not computation.
# When many I/O operations are happing at once.
# The asyncio module allows us to perform multiple tasks in parallel and iterate through them efficiently, without blocking the rest of the application.

# Some of the tasks are given below, which can work well with the asyncio.

# Web scraping.
# Network Services (web server and framework)
# Simultaneous Database

# Some Important Functions in Asyncio
# Below are the some essential methods that used while doing asynchronous programming.

# Running an asyncio Program
# asyncio.run(coro, *, debug = False) - This function is used to block the execution for delay seconds. It suspends the current task and allows another task to run. The delay is an argument that shows the number of seconds.
# Example -

# async def main():  
#     await asyncio.sleep(1)  
#     print('hello')  
# asyncio.run(main())  
# Creating Tasks
# create_task(coro, *, name = None) - This function wraps the Coroutines into a Task and schedule its execution. It returns the task object.
# Example -

# async def coro():  
#     ...  
  
# # In Python 3.7+  
# task = asyncio.create_task(coro())  
# ...  
# task = asyncio.ensure_future(coro())  
# Sleeping
# sleep(delay, result = None, *, loop = None) - This function is used to block the execution for delay seconds. It suspends the current task and allows other task to run. The delay is an argument which shows the number of seconds.
# Example -

# import asyncio  
# async def main():  
#     for _ in range(3):  
#         await asyncio.sleep(1)  
#         print ("Hello")  
# asyncio.run(main())  
# Timeouts
# coroutinewait_for(aw, timeout, *, loop = None) - This function is used to wait for the aw (a coroutine automatically schedule as a Task) awaitable to complete with a timeout.
# Example -

# async def myfunc():  
#     # Sleep for ten minutes  
#     await asyncio.sleep(600)  
#     print('hello!')  
  
# async def main():  
#     # Wait for at most 1 second  
#     try:  
#         await asyncio.wait_for(myfunc(), timeout=1.0)  
#     except asyncio.TimeoutError:  
#         print('timeout!')  
  
# asyncio.run(main())  