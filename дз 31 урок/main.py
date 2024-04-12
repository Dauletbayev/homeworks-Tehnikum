from threading import Thread

def red():
    print('Red light')

def yellow():
    print('Yellow light')

def green():
    print('Green light')

t1 = Thread(target=red)
t2 = Thread(target=yellow)
t3 = Thread(target=green)

t1.start()
t2.start()
t3.start()
