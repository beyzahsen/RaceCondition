from threading import Thread, Lock


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def earn(self):
        for _ in range(100000):
            self.lock.acquire() #threadlerde atomic parçalar oluşturuyor.
            self.balance += 1
            self.lock.release()
        print("Earned")

    def spend(self):
        for _ in range(100000):
            self.lock.acquire()
            self.balance -= 1
            self.lock.release()
        print("Spent")

    def get_balance(self):
        return self.balance


if __name__ == "__main__":
    bank_account = BankAccount()
    thread1 = Thread(target=bank_account.earn(), args=())
    thread2 = Thread(target=bank_account.spend(), args=())
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    current_balance = bank_account.get_balance()
    print(current_balance)
