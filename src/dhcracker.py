import math, utils as u

class Cracker:
    def __init__(self, dh):
        self.dh = dh # DH key exchange parameters needed for printing results
        self.prime = dh.prime # public prime
        self.generator = dh.generator # public generator
        self.pub_a = dh.pub_a # Alice's public parameter
        self.pub_b = dh.pub_b # Bob's public parameter
        self.timer = None
    
    def crack_bf(self): # Cracking DH protocol using bruteforce (not effective)
        self.timer = u.Timer("bruteforce")
        for pri_a in range(1, self.prime-1):
            tested_pub_a = pow(self.generator, pri_a, self.prime)
            if tested_pub_a == self.pub_a:
                self.timer.stop(pow(self.pub_b, pri_a, self.prime), self.dh.key_a)
                return

    def crack_bsgs(self): # Cracking DH protocol using baby-step giant-step algorithm
        self.timer = u.Timer("Baby-Step Giant-Step")
        pri_b = self.bsgs_algorithm(self.generator, self.prime, self.pub_b)
        if pri_b is None:
            self.timer.stop("Not found", self.key_b)
            return
        else:
            self.timer.stop(pow(self.pub_a, pri_b, self.prime), self.dh.key_b)

    def bsgs_algorithm(self, gen, prime, pub_param):
        """
        gen^pri_param mod prime = pub_param
        """
        ceiling = int(math.ceil(math.sqrt(prime-1)))
        # Baby step
        pairs = {}
        for i in range(ceiling):
            pairs[pow(gen, i, prime)] = i
        
        gen_inv = pow(gen, ceiling * (prime - 2), prime)
        y = pub_param

        # Giant step
        for i in range(ceiling):
            y = (pub_param * pow(gen_inv, i, prime)) % prime
            if y in pairs.keys():
                return i*ceiling+pairs[y]
        return None

    def crack_pol_rho(self):
        pass

    def __pollard_rho_algorithm(self):
        pass

    def getResults(self):
        return {
            "bitlen": self.dh.bitlen,
            "method": self.timer.method,
            "prime": self.prime,
            "generator": self.generator,
            "pri_a": self.dh.pri_a,
            "pri_b": self.dh.pri_b,
            "pub_a": self.dh.pub_a,
            "pub_b": self.dh.pub_b,
            "key_calc": self.timer.key_calc,
            "key_orig": self.timer.key_orig,
            "time_needed": self.timer.duration
        }
