import os, time, random
from multiprocessing import Process, Queue


# 寫數據進程執行代碼
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 讀數據進程執行的代碼
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 啟動子進程pw，寫入：
    pw.start()
    # 啟動子進程讀取
    pr.start()
    # 等待pw結束
    pw.join()
    # pr進程裏是死循環，無法等待其結束，只能強行終止
    pr.terminate()