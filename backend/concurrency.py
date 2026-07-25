'''
Concurrency
'''
import threading

counter = 0
lock = threading.Lock()


def increment():
    '''increment'''
    global counter

    for _ in range(100_000):
        with lock:
            counter += 1


threads = [
    threading.Thread(target=increment),
    threading.Thread(target=increment),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(counter)
