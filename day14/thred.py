import threading,time
def findsquare(getlist):
    for i in getlist:
        time.sleep(3) # intentially create a delay
        print(i*i)
def findcube(getlist):
    for i in getlist:
        time.sleep(3)
        print(i*i*i)
mylist=[2,3,4,5]
t1=threading.Thread(target=findsquare,args=(mylist,)) # create a thread
t2=threading.Thread(target=findcube,args=(mylist,)) # create a thread
t1.start()
t2.start()
t1.join()
t1.join()
print("...........")
# printNumbers()