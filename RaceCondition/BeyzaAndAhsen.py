import time
from threading import Thread, Lock


def beyza(lock1, lock2):
    while True:
        print("Beyza: Acquiring lock 1")
        lock1.acquire()
        print("Beyza: Acquiring lock 2")
        lock2.acquire()
        print("Beyza: locks acquired")
        lock1.release()
        lock2.release()
        print("Beyza: locks acquired")
        time.sleep(0.5)

def ahsen(lock1, lock2):
    while True:
        print("Ahsen: Acquiring lock 1")
        lock1.acquire()
        print("Ahsen: Acquiring lock 2")
        lock2.acquire()
        print("Ahsen: locks acquired")
        lock1.release()
        lock2.release()
        print("Ahsen: locks acquired")
        time.sleep(0.5)


if __name__ == "__main__":
    # mutual exclusive
    mutex1 = Lock()
    mutex2 = Lock()
    beyza_thread = Thread(target=beyza, args=(mutex1, mutex2))
    ahsen_thread = Thread(target=ahsen, args=(mutex1, mutex2))
    beyza_thread.start()
    ahsen_thread.start()
