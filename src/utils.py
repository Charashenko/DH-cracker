import time, math, sympy, random

class Timer:
    def __init__(self, algorithm):
        self.start = time.time()
        self.method = algorithm
        print(f"Started cracking using {algorithm}...")

    def stop(self, key_calc, key_orig):
        self.end = time.time()
        self.duration = round(self.end - self.start, 6)
        self.key_calc = key_calc
        self.key_orig = key_orig
        

def getPrime(bitlen):
    if bitlen < 2:
        return None
    p = 0
    while not sympy.isprime(p):
        p = random.getrandbits(bitlen)
    return p
    
def euler(self, n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount
