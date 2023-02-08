from typing import Callable, List
import time
from threading import Thread
from concurrent.futures import Future, ThreadPoolExecutor
from queue import Queue


def download_file(index: int):
    time.sleep(0.1)
    print(f"download_file ends [{index}]")


NUMBER_OF_FILES = 5


def print_elapsed_timer(action: Callable[[], None]):
    print(f"--- {action.__name__} ---")
    start = time.time()
    action()
    end = time.time()
    elapsed_time = end - start
    print(format(elapsed_time, ".3f"))


def without_thread():
    for index in range(NUMBER_OF_FILES):
        download_file(index)


def with_thread1():
    for index in range(NUMBER_OF_FILES):
        worker = Thread(target=download_file, daemon=True, args=[index])
        worker.daemon = True
        worker.start()
        worker.join()


def with_thread2():
    workers: List[Thread] = []
    for index in range(NUMBER_OF_FILES):
        worker = Thread(target=download_file, daemon=True, args=[index])
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()


def with_thread3():
    q = Queue(maxsize=3)

    def download_file_with_queue():
        while True:
            item = q.get()
            download_file(item)
            q.task_done()

    worker = Thread(target=download_file_with_queue, daemon=True)
    worker.start()

    for index in range(NUMBER_OF_FILES):
        q.put(index, block=True, timeout=None)
    q.join()


def with_thread4():
    q1 = Queue(maxsize=3)
    q2 = Queue(maxsize=3)

    def download_file_with_queue(q: Queue, num: int):
        while True:
            item = q.get()
            download_file(num + item)
            q.task_done()

    Thread(target=download_file_with_queue, daemon=True, args=[q1, 10]).start()
    Thread(target=download_file_with_queue, daemon=True, args=[q2, 20]).start()

    for index in range(NUMBER_OF_FILES):
        q1.put(index, block=True, timeout=None)
        q2.put(index, block=True, timeout=None)
    q1.join()
    q2.join()


def with_thread5():
    executor = ThreadPoolExecutor(max_workers=3)
    for index in range(NUMBER_OF_FILES):
        executor.submit(download_file, index)

    executor.shutdown()

def with_thread6():
    executor = ThreadPoolExecutor(max_workers=30)

    def download_file_with_returned_value(index):
        download_file(index)
        return f"returned value: {index}"

    futures: List[Future] = []
    for index in range(NUMBER_OF_FILES):
        future = executor.submit(download_file_with_returned_value, index)
        futures.append(future)

    executor.shutdown()
    print("finish the process")
    for future in futures:
        print(future.result())

# print_elapsed_timer(without_thread)
# print_elapsed_timer(with_thread1)
# print_elapsed_timer(with_thread2)
# print_elapsed_timer(with_thread3)
# print_elapsed_timer(with_thread4)
# print_elapsed_timer(with_thread5)
print_elapsed_timer(with_thread6)
