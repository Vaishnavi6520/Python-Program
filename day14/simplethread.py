import threading,time
def printNumbers():
    for i in range(1,4):
        time.sleep(3) # intentially create a delay
        print(i)
def printHello():
    for i in range(1,4):
        time.sleep(3)
        print("Hello")
t1=threading.Thread(target=printNumbers) # create a thread
t2=threading.Thread(target=printHello) # create a thread
t1.start()
t2.start()
t1.join()
t1.join()
print("...........")
# printNumbers()