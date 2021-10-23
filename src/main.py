import dhprotocol as dhp
import threading as th
import concurrent.futures as cf

def exec(i):
    dh_protocol = dhp.DiffieHellman(int(i))
    print(dh_protocol)

<<<<<<< HEAD
with cf.ThreadPoolExecutor(max_workers=20) as executor: # S multithreadingom
    executor.map(exec, range(11, 30))

#for i in range(11, 30): # bez multithreadingu
#    exec(i)
=======
#with cf.ThreadPoolExecutor(max_workers=20) as executor: # S multithreadingom
#    executor.map(exec, range(10, 30))

for i in range(2, 50): # bez multithreadingu
    exec(i)

>>>>>>> 771e7b2 (performance tweaks)
