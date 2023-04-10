import threading, random, time

def task():
    semaforo.acquire()
    number_sleep = random.randint(1, 5)
    time.sleep(number_sleep)
    print(f"olá, sou a task {number_sleep}")
    semaforo.release()

threads = []
for i in range(3):
    thread = threading.Thread(target=task)
    threads.append(thread)

semaforo = threading.Semaphore(2)
for thread in threads:
    thread.start()
    thread.join()

