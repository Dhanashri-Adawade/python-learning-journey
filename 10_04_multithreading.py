import threading
import time

def worker(num):
    print(f"thread {num}: Starting")
    time.sleep(5)
    print(f"thread {num}: Finshing")

threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all threads completed")