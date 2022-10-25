import threading, time
from PyQt6 import uic, QtWidgets
from Form import Ui_Dialog
from random import randint

norm = 500

def counter_s(who):
    global norm
    while True:
        b = randint(-5,0)
        norm += b
        print(f'\n{who} изменил(a) текущие значение на {b}, счётчик равен {norm}')
        time.sleep(1)

def counter_r(who):
    global norm
    while True:
        b = randint(0,5)
        norm += b
        print(f'\n{who} изменил(a) текущие значение на {b}, счётчик равен {norm}')
        time.sleep(1)


def manual_change(who):
    global norm
    while True:
        try:
            b = int(input())
        except:
            b = norm
        else:
            norm = b
        print(f'{who} заменил(a) текущие значение на {abs(b)}, счётчик равен {norm}')


def main():
    t1 = threading.Thread(target=counter_s, args=('Стержень',))
    t2 = threading.Thread(target=counter_r, args=('Реакция',))
    t3 = threading.Thread(target=manual_change, args=('Оператор',))
    t1.start()
    t2.start()
    t3.start()


if __name__ == "__main__":
    main()