import time,os
os.system('cls')

tme = 0.1 # time between frames

Loop_Amount=5 # variable for amount of full loops

x=0 # variable used to start and stop loops
while True:
    print('o-----',end='\r')
    time.sleep(tme)
    print('-o----',end='\r')
    time.sleep(tme)
    print('--o---',end='\r')
    time.sleep(tme)
    print('---o--',end='\r')
    time.sleep(tme)
    print('----o-',end='\r')
    time.sleep(tme)
    print('-----o',end='\r')
    time.sleep(tme)
    print('-----o',end='\r')
    time.sleep(tme)
    print('----o-',end='\r')
    time.sleep(tme)
    print('---o--',end='\r')
    time.sleep(tme)
    print('--o---',end='\r')
    time.sleep(tme)
    print('-o----',end='\r')
    time.sleep(tme)
    print('o-----',end='\r')
    time.sleep(tme)
    x += 1
    if x>=Loop_Amount:
        break
x=0
