from multiprocessing import Pool
import threading
import time

# Creating a sub-class extending the thread class

# exitFlag = 0


# class MyThreads(threading.Thread):
#     # Overiding the __init__ method
#     def __init__(self, thread_number, thread_name, thread_delay):
#         threading.Thread.__init__(self)
#         self.thread_number = thread_number
#         self.thread_name = thread_name
#         self.thread_delay = thread_delay

#     # defining our own run method
#     def run(self):
#         print("Starting", self.thread_name)
#         print_time(self.thread_name, self.thread_delay, counter=5)
#         print("Ending", self.thread_name)


# def print_time(thread_name, delay, counter):
#     while counter:
#         if exitFlag:
#             thread_name.exit()
#         time.sleep(delay)
#         print(f'{thread_name} running at {time.ctime(time.time())}')
#         counter -= 1


# thread1 = MyThreads(1, "thread1", 2)
# thread2 = MyThreads(2, "thread2", 2)

# thread1.start()
# thread2.start()
lock = threading.Lock()


def print_my_name(name):
    counter = 5
    lock.acquire()
    while counter:
        print(name)
        counter -= 1
    lock.release()


def print_my_surname(surname):
    counter = 5
    lock.acquire()
    while counter:
        print(surname)
        counter -= 1
    lock.release()


thread1 = threading.Thread(target=print_my_name, args=("Kumar",))
thread2 = threading.Thread(target=print_my_surname, args=("Maiti",))

thread1.start()
thread2.start()

threads = []
threads.append(thread1)
threads.append(thread2)

for thread in threads:
    thread.join()

# Multi-threading is useful because it can run multiple-threads concurrently and also share the same data space with the main thread. This allows to share information and update the same variable. They can communicate with each other. They are lightweight than multiple process.


def is_prime(n):
    if n < 2:
        return 0
    if n < 4:
        return 1
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


if __name__ == "__main__":
    start = time.time()
    answer = 0
    for i in range(100000):
        answer += is_prime(i)

    print(answer)
    end = time.time()
    print(end-start, "s")

    p = Pool()
    start = time.time()
    result = sum(p.map(is_prime, range(100000)))
    end = time.time()
    print(result)
    print(end-start, "s")
