import threading, random, time, psutil

def memory_ram_stats():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_usage_mb = memory_info.rss / 1024 / 1024

    print(f"total RAM: {memory_usage_mb:.2f} MB")

def task():
    semaforo.acquire()
    number_sleep = random.randint(1, 5)
    time.sleep(number_sleep)
    print(f"olá, sou a task {number_sleep}")
    memory_ram_stats()
    semaforo.release()
    

threads = []
for i in range(3):
    thread = threading.Thread(target=task)
    threads.append(thread)

semaforo = threading.Semaphore(2)
for thread in threads:
    thread.start()
    thread.join()

