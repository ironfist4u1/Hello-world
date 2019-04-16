from threading import Thread
import threading
import time
import random
lock = threading.Lock()

holder = 0


class roller(Thread):
    def __init__(self,num,div):
        Thread.__init__(self,name="roller")
        self._num = 0
        self._div = 0
        self._num = num
        self._div = div

    def run(self):#locks not required since we are only ever doing add/sub
        global holder
        random.seed()
        new = random.randint(1,10)
        #lock.acquire()
        if new == 10:
            holder = holder + 1
            rol = roller(self._num,self._div)
            rol.daemon = True
            rol.start()
        elif new >= self._div:
            holder += 1
        elif new == 1:
            holder -= 1
        #lock.release()
        
        


def reroll(div,wins,box):
    random.seed()
    new = random.randint(1,10)
    box.append(new)
    if new == 10:
        wins+=1
        reroll(div,wins,box)
    elif new >= div:
        wins+=1
        return 0
    elif new == 1:
        wins-=1
        return 0

def dice(num,div):
    random.seed()
    box = []
    while num >= 0:
        box.append(random.randint(1,10))
        num-=1

    wins = 0
    for i in range(0,len(box)):
        if box[i] >= div and not box[i] == 10:
            wins+=1
        elif box[i] == 1:
            wins-=1
        elif box[i] == 10:
            wins+=1
            reroll(div,wins,box)

    returner = str(wins)
    return wins


def adv(num,div):
    global holder
    low = 99999999
    high = -999999999
    avg = 0
    start = time.time()
    for i in range(0,100):
        for i in range(0,num):
            rol = roller(num,div)
            rol.daemon = True
            rol.start()
        #number = dice(num,div) #is the faster of the two
        avg+= holder
        if  holder > high:
            high = holder
        elif  holder < low:
            low = holder
        holder = 0
        del(rol)
    avg = avg/100
    end = time.time()
    print(end-start)
    return "%s high and %s avg and %s low" % (high,avg,low)
