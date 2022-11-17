import math
import threading, time
from PyQt6 import uic, QtWidgets
from random import randint
import math as ma
import sympy as sy
import numpy as np
from time import *

b = math.pi
step = 10e-6
count = int((b // step) // 100)

def integral(p):
    x = sy.Symbol('x')
    y = sy.cos(x)
    a = 0
    b = math.pi
    Y = sy.integrate(y, (x, a, b))
    strap = 0
    step = 10e-6
    global count
    count = int((b // step))
    ai = a
    bi = step
    while count != 0:
        h = y.subs(x, (ai + bi) / 2)
        strap += 0.5 * (y.subs(x, ai) + y.subs(x, bi)) * step
        ai = bi
        bi += step
        count -= 1
        print('',end='')


def main():
    for p in range(2, 12, 2):
        threads = [threading.Thread(target=integral, args=(p,)) for i in range(1, p+1)]
        start = time()
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        stop = time()
        print(f'{p} потоков - {stop - start} мс.')


if __name__ == "__main__":
    main()