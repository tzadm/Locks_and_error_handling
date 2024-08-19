from time import sleep
import threading
from random import randint


class Bank:
    balance = 0
    lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            num = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += num
            print(f'Пополнение: {num}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        from random import randint
        for i in range(100):
            num = randint(50, 500)
            from time import sleep
            print(f'Запрос на {num}')
            if num <= self.balance:
                self.balance -= num
                print(f'Снятие: {num}. Баланс: {self.balance}')
            if num > self.balance:
                if self.lock.locked() is False:
                    self.lock.acquire()
                    print(f'Запрос отклонён, недостаточно средств')
                elif self.lock.locked():
                    print(f'Запрос отклонён, недостаточно средств')
            sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
