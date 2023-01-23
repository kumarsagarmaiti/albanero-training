# GIL is a mutex lock in python which allows only one thread to execute at a time. This is why python is a single-threaded application. So if your program is single threaded python will perform as equal to any other language. But when it comes to multithreading and executing threads in parallel, it is not possible in python. Python supports multi-processing but not multi-threading.
# Why GIL?
# Python uses reference counting for memory management. What it does is keeps track of all the variables that are created and whether they are being used in the program now or not. If there is no reference for those variables. The python garbage collector kicks in and removes that variable from the heap.

# Now for this reference counting to work properly it needs to be safe from race conditions. That is two threads try to change the reference count. If that happens that can lead to a memory leak. This reference count can be kept safe by locking all the data structures that are shared across the threads.

# Now if we lock these data structures. It means multiple locks will exist which can lead to problems like a deadlock. Also, it will decrease performance as acquisition and release of locks will happen quite frequently.

# GIL is a single lock that says that execution of any python byte code requires the interpreter lock. This prevents the above problem but makes the python single-threaded.

# The threading Module
# We can still perform multi-threading using the threading module. Multiple threads within a process share the same data space with the main thread and can therefore share information or communicate with each other more easily than if they were separate processes.

# The newer threading module included with Python 2.4 provides much more powerful, high-level support for threads than the thread module discussed in the previous section.

# The threading module exposes all the methods of the thread module and provides some additional methods −

# threading.activeCount() − Returns the number of thread objects that are active.

# threading.currentThread() − Returns the number of thread objects in the caller's thread control.

# threading.enumerate() − Returns a list of all thread objects that are currently active.

# The threading module has the Thread class that implements threading. The methods provided by the Thread class are as follows −

# run() − The run() method is the entry point for a thread.

# start() − The start() method starts a thread by calling the run method.

# join([time]) − The join() waits for threads to terminate.

# isAlive() − The isAlive() method checks whether a thread is still executing.

# getName() − The getName() method returns the name of a thread.

# setName() − The setName() method sets the name of a thread.

# Example
# The threading module provided with Python includes a simple-to-implement locking mechanism that allows you to synchronize threads. A new lock is created by calling the Lock() method, which returns the new lock.

# The acquire(blocking) method of the new lock object is used to force the threads to run synchronously. The optional blocking parameter enables you to control whether the thread waits to acquire the lock.

# If blocking is set to 0, the thread returns immediately with a 0 value if the lock cannot be acquired and with a 1 if the lock was acquired. If blocking is set to 1, the thread blocks and wait for the lock to be released.

# The release() method of the new lock object is used to release the lock when it is no longer required.

import threading
import time


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # Free lock to release next thread
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")
