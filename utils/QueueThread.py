#coding:utf-8

import threading
import Queue


class QueueThread:

    def __init__(self, method, consumer_nums, list_par):
        self.method = method
        self.consumer_nums = consumer_nums
        self.queue_max_nums = consumer_nums
        self.producer_nums = 1
        self.list_par = list_par
        self.result = []

        self.q = Queue.Queue(self.queue_max_nums)

    def run(self):
        self.threads = []
        for i in range(self.producer_nums):
            t = threading.Thread(target=self.producter)
            self.threads.append(t)
        for i in range(self.consumer_nums):
            t = threading.Thread(target=self.consumer)
            self.threads.append(t)
        for t in self.threads:
            t.start()
        for t in self.threads:
            t.join()

    def producter(self):
        for par in self.list_par:
            self.q.put(par)

    def consumer(self):
        while True:
            try:
                self.result.append(self.method(self.q.get(timeout=4)))
            except:
                break

if __name__ == '__main__':
    q = QueueThread(1, 4, [1,2,3,4,5,6])
    q.run()
    print(q.result)

