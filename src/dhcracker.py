import time
from concurrent.futures import ThreadPoolExecutor as TPE

class Cracker:
    def __init__(self, dh):
        self.prime = dh.prime # public prime
        self.generator = dh.generator # public generator
        self.pub_a = dh.pub_a # Alice's public parameter
        self.pub_b = dh.pub_b # Bob's public parameter
        self.key = dh.key_a # Searched key
    
    def crack_bf(self):
        start = time.time()
        for pri_a in range(1, self.prime-1): # 
            tested_key = pow(self.pub_b, pri_a, self.prime)
            if tested_key == self.key:
                print(f"Found key in > {time.time()-start}")
                print(f"Key is > {tested_key}")
                return True

