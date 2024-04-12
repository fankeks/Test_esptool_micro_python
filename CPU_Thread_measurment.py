from threading import Thread
import time
import random
import matplotlib.pyplot as plt
import numpy as np


def th(arr1, arr2, start, stop):
    for i in range(start, stop):
        arr1[i] + arr2[i]

def plot_graph():
    ns = [10000, 50000, 100000, 200000, 400000, 800000]
    times_thread = []
    times = []
    for n in ns:
        arr1 = [random.random() for _ in range(n)]
        arr2 = [random.random() for _ in range(n)]

        t1 = Thread(target=th, args=(arr1, arr2, 0, n))
        t2 = Thread(target=th, args=(arr1, arr2, 0, n))

        # Измерение времени с потоками
        start_time = time.time()
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        times_thread.append(time.time() - start_time)

        # Измерение времени без потоков
        start_time = time.time()
        th(arr1, arr2, 0, n)
        th(arr1, arr2, 0, n)
        times.append(time.time() - start_time)

    plt.plot(ns, np.array(times_thread) * 1000, label='С потоками')
    plt.plot(ns, np.array(times) * 1000, label='Без потоков')
    plt.legend()
    plt.ylabel('Время [мс]')
    plt.xlabel('Колличество эллементов в массивах')
    plt.savefig('График.png', dpi=512)
    plt.show()


if __name__ == '__main__':
    plot_graph()