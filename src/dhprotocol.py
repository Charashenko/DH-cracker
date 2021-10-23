import random, math
import sympy as sp

class DiffieHellman:
    def __init__(self, bitlen):
        self.bitlen = bitlen # bit length of wanted prime number
        self.prime = self.__getPrime(bitlen) # public prime number
        self.generator = random.getrandbits(10) # public generator
        self.pri_a = random.randint(1, self.prime-1) # Alice's private parameter
        self.pri_b = random.randint(1, self.prime-1) # Bob's private parameter
        self.pub_a = self.generator**self.pri_a % self.prime # Alice's public parameter
        self.pub_b = self.generator**self.pri_b % self.prime # Bob's public parameter
        self.key_a = self.pub_b**self.pri_a % self.prime # Alice's final private key
        self.key_b = self.pub_a**self.pri_b % self.prime # Bob's final private key

    def __getPrime(self,bitlen):
        p = 0
        while not sp.isprime(p):
            p = random.getrandbits(bitlen)
        return p

    def __str__(self):
        return str("################\n"
            + f"Bit length > {self.bitlen}\n"
            + f"Prime > {self.prime}\n"
            + f"Generator > {self.generator}\n"
            + f"Private_A > {self.pri_a}\n"
            + f"Private_B > {self.pri_b}\n"
            + f"Public_A > {self.pub_a}\n"
            + f"Public_B > {self.pub_b}\n"
            + f"Key_A > {self.key_a}\n"
            + f"Key_B > {self.key_b}")

