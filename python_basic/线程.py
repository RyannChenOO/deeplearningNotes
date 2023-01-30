import time
import threading
g_table = list(range(100))  # 全局表
lock = threading.Lock()  # 创建Lock锁


def squ(begin, end):
    for i in range(begin, end+1):
        lock.acquire()  # 获取锁
        global g_table
        g_table[i] = g_table[i] ** 2
        time.sleep(1)
        lock.release()  # 释放锁


if __name__ == "__main__":
    print("Thread %s is running." % threading.current_thread().name)  # 主线程
    thread_list = []
    for i in range(10):
        t = threading.Thread(target=squ, args=(
            i*10, (i+1)*10))  # 实例化Thread类，创建线程
        thread_list.append(t)
    for t in thread_list:  # 启动所有线程
        t.start()

    time.sleep(1)
    print(g_table)
