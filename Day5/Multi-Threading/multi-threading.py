# In computing, a process is an instance of a computer program that is being executed. Any process has 3 basic components:

# An executable program.
# The associated data needed by the program (variables, work space, buffers, etc.)
# The execution context of the program (State of process)

# A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS (Operating System). In simple words, a thread is a sequence of such instructions within a program that can be executed independently of other code. For simplicity, you can assume that a thread is simply a subset of a process!

# Multi-threading: Multiple threads can exist within one process where:

# Each thread contains its own register set and local variables (stored in stack).
# All threads of a process share global variables (stored in heap) and the program code.
# Multithreading is defined as the ability of a processor to execute multiple threads concurrently.

# Running several threads is similar to running several different programs concurrently, but with the following benefits −

# Multiple threads within a process share the same data space with the main thread and can therefore share information or communicate with each other more easily than if they were separate processes.
# Threads sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.

# A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context it is currently running.

# It can be pre-empted (interrupted)
# It can temporarily be put on hold (also known as sleeping) while other threads are running - this is called yielding.

# The newer threading module included with Python 2.4 provides much more powerful, high-level support for threads than the thread module.

# The threading module exposes all the methods of the thread module and provides some additional methods −

# threading.activeCount() − Returns the number of thread objects that are active.
# threading.currentThread() − Returns the number of thread objects in the caller's thread control.
# threading.enumerate() − Returns a list of all thread objects that are currently active.

# In addition to the methods, the threading module has the Thread class that implements threading. The methods provided by the Thread class are as follows −

# run() − The run() method is the entry point for a thread.
# start() − The start() method starts a thread by calling the run method.
# join([time]) − The join() waits for threads to terminate.
# isAlive() − The isAlive() method checks whether a thread is still executing.
# getName() − The getName() method returns the name of a thread.
# setName() − The setName() method sets the name of a thread.

# Creating Thread Using Threading Module
# To implement a new thread using the threading module, you have to do the following −

# Define a new subclass of the Thread class.

# Override the __init__(self [,args]) method to add additional arguments.

# Then, override the run(self [,args]) method to implement what the thread should do when started.

# Once you have created the new Thread subclass, you can create an instance of it and then start a new thread by invoking the start(), which in turn calls run() method.

# Example
#!/usr/bin/python

# import threading
# import time

# exitFlag = 0

# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print "Starting " + self.name
#       print_time(self.name, 5, self.counter)
#       print "Exiting " + self.name

# def print_time(threadName, counter, delay):
#    while counter:
#       if exitFlag:
#          threadName.exit()
#       time.sleep(delay)
#       print "%s: %s" % (threadName, time.ctime(time.time()))
#       counter -= 1

# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# # Start new Threads
# thread1.start()
# thread2.start()

# print "Exiting Main Thread"
# When the above code is executed, it produces the following result −

# Starting Thread-1
# Starting Thread-2
# Exiting Main Thread
# Thread-1: Thu Mar 21 09:10:03 2013
# Thread-1: Thu Mar 21 09:10:04 2013
# Thread-2: Thu Mar 21 09:10:04 2013
# Thread-1: Thu Mar 21 09:10:05 2013
# Thread-1: Thu Mar 21 09:10:06 2013
# Thread-2: Thu Mar 21 09:10:06 2013
# Thread-1: Thu Mar 21 09:10:07 2013
# Exiting Thread-1
# Thread-2: Thu Mar 21 09:10:08 2013
# Thread-2: Thu Mar 21 09:10:10 2013
# Thread-2: Thu Mar 21 09:10:12 2013
# Exiting Thread-2

# Synchronizing Threads
# The threading module provided with Python includes a simple-to-implement locking mechanism that allows you to synchronize threads. A new lock is created by calling the Lock() method, which returns the new lock.

# The acquire(blocking) method of the new lock object is used to force threads to run synchronously. The optional blocking parameter enables you to control whether the thread waits to acquire the lock.

# If blocking is set to 0, the thread returns immediately with a 0 value if the lock cannot be acquired and with a 1 if the lock was acquired. If blocking is set to 1, the thread blocks and wait for the lock to be released.

# The release() method of the new lock object is used to release the lock when it is no longer required.

# Example
# #!/usr/bin/python

# import threading
# import time

# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print "Starting " + self.name
#       # Get lock to synchronize threads
#       threadLock.acquire()
#       print_time(self.name, self.counter, 3)
#       # Free lock to release next thread
#       threadLock.release()

# def print_time(threadName, delay, counter):
#    while counter:
#       time.sleep(delay)
#       print "%s: %s" % (threadName, time.ctime(time.time()))
#       counter -= 1

# threadLock = threading.Lock()
# threads = []

# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# # Start new Threads
# thread1.start()
# thread2.start()

# # Add threads to thread list
# threads.append(thread1)
# threads.append(thread2)

# # Wait for all threads to complete
# for t in threads:
#     t.join()
# print "Exiting Main Thread"
# When the above code is executed, it produces the following result −

# Starting Thread-1
# Starting Thread-2
# Thread-1: Thu Mar 21 09:11:28 2013
# Thread-1: Thu Mar 21 09:11:29 2013
# Thread-1: Thu Mar 21 09:11:30 2013
# Thread-2: Thu Mar 21 09:11:32 2013
# Thread-2: Thu Mar 21 09:11:34 2013
# Thread-2: Thu Mar 21 09:11:36 2013
# Exiting Main Thread

# Multithreaded Priority Queue
# The Queue module allows you to create a new queue object that can hold a specific number of items. There are following methods to control the Queue −

# get() − The get() removes and returns an item from the queue.
# put() − The put adds item to a queue.
# qsize() − The qsize() returns the number of items that are currently in the queue.
# empty() − The empty( ) returns True if queue is empty; otherwise, False.
# full() − the full() returns True if queue is full; otherwise, False.

# Example
# #!/usr/bin/python

# import Queue
# import threading
# import time

# exitFlag = 0

# class myThread (threading.Thread):
#    def __init__(self, threadID, name, q):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.q = q
#    def run(self):
#       print "Starting " + self.name
#       process_data(self.name, self.q)
#       print "Exiting " + self.name

# def process_data(threadName, q):
#    while not exitFlag:
#       queueLock.acquire()
#          if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print "%s processing %s" % (threadName, data)
#          else:
#             queueLock.release()
#          time.sleep(1)

# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = Queue.Queue(10)
# threads = []
# threadID = 1

# # Create new threads
# for tName in threadList:
#    thread = myThread(threadID, tName, workQueue)
#    thread.start()
#    threads.append(thread)
#    threadID += 1

# # Fill the queue
# queueLock.acquire()
# for word in nameList:
#    workQueue.put(word)
# queueLock.release()

# # Wait for queue to empty
# while not workQueue.empty():
#    pass

# # Notify threads it's time to exit
# exitFlag = 1

# # Wait for all threads to complete
# for t in threads:
#    t.join()
# print "Exiting Main Thread"
# When the above code is executed, it produces the following result −

# Starting Thread-1
# Starting Thread-2
# Starting Thread-3
# Thread-1 processing One
# Thread-2 processing Two
# Thread-3 processing Three
# Thread-1 processing Four
# Thread-2 processing Five
# Exiting Thread-3
# Exiting Thread-1
# Exiting Thread-2
# Exiting Main Thread

# importing the threading module
# import threading


# def print_cube(num):
#     # function to print cube of given num
#     print("Cube: {}" .format(num * num * num))


# def print_square(num):
#     # function to print square of given num
#     print("Square: {}" .format(num * num))


# if __name__ =="__main__":
#     # creating thread
#     t1 = threading.Thread(target=print_square, args=(10,))
#     t2 = threading.Thread(target=print_cube, args=(10,))

#     # starting thread 1
#     t1.start()
#     # starting thread 2
#     t2.start()

#     # wait until thread 1 is completely executed
#     t1.join()
#     # wait until thread 2 is completely executed
#     t2.join()

#     # both threads completely executed
#     print("Done!")
# Square: 100
# Cube: 1000
# Done!
# Let us try to understand the above code:

# To import the threading module, we do:
# import threading
# To create a new thread, we create an object of Thread class. It takes following arguments:
# target: the function to be executed by thread
# args: the arguments to be passed to the target function
# To start a thread, we use start method of Thread class.
# t1.start()
# t2.start()
# Once the threads start, the current program (you can think of it like a main thread) also keeps on executing. In order to stop execution of current program until a thread is complete, we use join method.
# t1.join()
# t2.join()
# As a result, the current program will first wait for the completion of t1 and then t2. Once, they are finished, the remaining statements of current program are executed.

# Consider the python program given below in which we print thread name and corresponding process for each task:

# import threading
# import os

# def task1():
#     print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
#     print("ID of process running task 1: {}".format(os.getpid()))

# def task2():
#     print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
#     print("ID of process running task 2: {}".format(os.getpid()))

# if __name__ == "__main__":

#     # print ID of current process
#     print("ID of process running main program: {}".format(os.getpid()))

#     # print name of main thread
#     print("Main thread name: {}".format(threading.current_thread().name))

#     # creating threads
#     t1 = threading.Thread(target=task1, name='t1')
#     t2 = threading.Thread(target=task2, name='t2')

#     # starting threads
#     t1.start()
#     t2.start()

#     # wait until all threads finish
#     t1.join()
#     t2.join()

# Output:
# ID of process running main program: 11758
# Main thread name: MainThread
# Task 1 assigned to thread: t1
# ID of process running task 1: 11758
# Task 2 assigned to thread: t2
# ID of process running task 2: 11758
# Let us try to understand the above code:

# We use os.getpid() function to get ID of current process.
# print("ID of process running main program: {}".format(os.getpid()))
# As it is clear from the output, the process ID remains the same for all threads.
# We use threading.main_thread() function to get the main thread object. In normal conditions, the main thread is the thread from which the Python interpreter was started. name attribute of thread object is used to get the name of thread.
# print("Main thread name: {}".format(threading.main_thread().name))
# We use the threading.current_thread() function to get the current thread object.
# print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
