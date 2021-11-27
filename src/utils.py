import time, math, sympy, random

class Timer:
    def __init__(self, algorithm):
        print(f"Started cracking using {algorithm}...")
        self.start = time.time()

    def stop(self, key1, key2):
        self.end = time.time()
        self.duration = self.end - self.start
        print(f"Found key in > {round(self.duration, 6)}s")
        print(f"Calculated key > {key1}")
        print(f"Original key > {key2}")


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
