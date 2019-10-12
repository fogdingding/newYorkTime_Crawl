from BaseThread import BaseThread
import threading
import time

# 多執行緒的前工作
def my_thread_job():
    with sem:
        print("{} runing".format("hi"))
        time.sleep(1)
# 多執行緒的後工作
def cb(argv1, argv2):
    with sem:
        print("{} {}".format(argv1, argv2))


sem=threading.Semaphore(4)

for i in range(5):
    BaseThread(
    name = 'test',
    target=my_thread_job,
    callback=cb,
    callback_args=("hello","word")
    ).start()