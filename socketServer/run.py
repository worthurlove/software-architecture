import os
import random
import time
from multiprocessing import Pool
 
 
def worker(msg):
    print("%s开始执⾏,进程号为%d" % (msg, os.getpid()))
 
    # random.random()随机⽣成0~1之间的浮点数
    cmd = 'python client.py'
    os.system(cmd)
    print(msg, "执⾏完毕，耗时%" )
 
 
if __name__ == "__main__":  # 在win10 里必须要添加这一条件
    po = Pool(10)  # 定义⼀个进程池，最⼤进程数3
    for i in range(0, 10):
        # Pool.apply_async(要调⽤的⽬标,(传递给⽬标的参数元祖,))
        po.apply_async(worker, (i,))
    print("----start----")
    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()  # 等待po中所有⼦进程执⾏完成，必须放在close语句之后
    print("-----end-----")
