import time
import multiprocessing
def operation(n):
    total=0
    for i in range(n+1):
        total+=i**2
    return total
t1=time.time()
tasks=[3242323,342443223,24324234]
processes=[]
for task in tasks:
    process=multiprocessing.Process(target=operation,args=[task])
    process.start()
    processes.append(process)
for pr in processes:
    pr.join()
t2=time.time()
print(t2-t1)