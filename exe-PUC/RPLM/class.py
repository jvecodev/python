

# import time
# from threading import Thread
# def minhaThread():
#     for i in range(0, 10):
#         time.sleep(2)
#         print('Oi... estou aqui também')
# Thread(target=minhaThread).start()
# while True:
#     print('Estou rodando...')
#     time.sleep(.5)
from time import sleep
from threading import Thread
def minhaThread(parametro, t):
    for i in range(0, 10):
        
        print()
        print(parametro)
        sleep(t)
Thread(target=minhaThread, args=('T1: Oi... estou aqui também ', 1)).start()
Thread(target=minhaThread, args=('T2: Sou a segunda Thread... ', .5)).start()
while True:
    print('Estou rodando...')
    sleep(.5)


