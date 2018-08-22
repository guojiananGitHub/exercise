import time
import threading

# 假設這是你的銀行存款
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存後取，結果應該為0
    global balance
    balance = balance + n
    balance = balance - n


# def run_thread(n):
#     for i in range(100000):
#         change_it(n)

def run_thread(n):
    for i in range(100000):
        # 先要獲取鎖
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)