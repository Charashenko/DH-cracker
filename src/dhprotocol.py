import random, math, utils

class DiffieHellman:
    def __init__(self, bitlen):
        self.bitlen = bitlen # bit length of wanted prime number
        self.prime = utils.getPrime(bitlen) # public prime number
        self.generator = self.__getGenerator(self.prime) # public generator
        self.pri_a = random.randint(1, self.prime-1) # Alice's private parameter
        self.pri_b = random.randint(1, self.prime-1) # Bob's private parameter
        self.pub_a = pow(self.generator, self.pri_a, self.prime) # Alice's public parameter
        self.pub_b = pow(self.generator, self.pri_b, self.prime) # Bob's public parameter
        self.key_a = pow(self.pub_b, self.pri_a, self.prime) # Alice's final private key
        self.key_b = pow(self.pub_a, self.pri_b, self.prime) # Bob's final private key

    def __str__(self):
        return str("\n################\n"
            + f"Bit length > {self.bitlen}\n"
            + f"Prime > {self.prime}\n"
            + f"Generator > {self.generator}\n"
            + f"Private_A > {self.pri_a}\n"
            + f"Private_B > {self.pri_b}\n"
            + f"Public_A > {self.pub_a}\n"
            + f"Public_B > {self.pub_b}\n"
            + f"Key_A > {self.key_a}\n"
            + f"Key_B > {self.key_b}")

    def __getGenerator(self, prime): # This code was borrowed from user kasravnd at https://stackoverflow.com/questions/40190849
        required_set = {num for num in range(1, prime) if math.gcd(num, prime)}
        for g in range(prime, 1, -1):
            if required_set == {pow(g, powers, prime) for powers in range(1, prime)}:
                return g
