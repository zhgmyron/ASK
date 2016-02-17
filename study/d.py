# -*- coding: UTF-8 -*-
import thread
import time
import threading
# 一个用于在线程中执行的函数
def func():
    for i in range(5):
        print 'func'

    print lock.locked()
    # 结束当前线程
    # 这个方法与thread.exit_thread()等价
    thread.exit() # 当func返回时，线程同样会结束
lock = thread.allocate()
# 启动一个线程，线程立即开始运行
# 这个方法与thread.start_new_thread()等价
# 第一个参数是方法，第二个参数是方法的参数
thread.start_new(func, ()) # 方法没有参数时需要传入空tuple

# 创建一个锁（LockType，不能直接实例化）
# 这个方法与thread.allocate_lock()等价


# 判断锁是锁定状态还是释放状态
print lock.locked()

# 锁通常用于控制对共享资源的访问
count = 0

# 获得锁，成功获得锁定后返回True
# 可选的timeout参数不填时将一直阻塞直到获得锁定
# 否则超时后将返回False
if lock.acquire():
    count += 1
    print lock.locked()
    print " 11"
    # 释放锁
    lock.release()

# thread模块提供的线程都将在主线程结束后同时结束




# 方法1：将要执行的方法作为参数传给Thread的构造方法
def func():
    print 'func() passed to Thread'

t = threading.Thread(target=func)
t.start()

# 方法2：从Thread继承，并重写run()
class MyThread(threading.Thread):
    def run(self):
        print 'MyThread extended from Thread'



data = 0
lock = threading.Lock()

def fun():
    global data
    print '%s acquire lock...' % threading.currentThread().getName()

    # 调用acquire([timeout])时，线程将一直阻塞，
    # 直到获得锁定或者直到timeout秒后（timeout参数可选）。
    # 返回是否获得锁。
    if lock.acquire():
        print '%s get the lock.' % threading.currentThread().getName()
        data += 1
        time.sleep(2)
        print '%s release lock...' % threading.currentThread().getName()

        # 调用release()将释放锁。
        lock.release()

rlock = threading.RLock()

def func():
    # 第一次请求锁定
    print '%s acquire lock...' % threading.currentThread().getName()
    if rlock.acquire():
        print '%s get the lock.' % threading.currentThread().getName()
        time.sleep(2)

        # 第二次请求锁定
        print '%s acquire lock again...' % threading.currentThread().getName()
        if rlock.acquire():
            print '%s get the lock.' % threading.currentThread().getName()
            time.sleep(2)

        # 第一次释放锁
        print '%s release lock...' % threading.currentThread().getName()
        rlock.release()
        time.sleep(2)

        # 第二次释放锁
        print '%s release lock...' % threading.currentThread().getName()
        rlock.release()

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t1.start()
t2.start()
t3.start()