import math, utils as u

class Cracker:
    def __init__(self, dh):
        self.prime = dh.prime # public prime
        self.generator = dh.generator # public generator
        self.pub_a = dh.pub_a # Alice's public parameter
        self.pub_b = dh.pub_b # Bob's public parameter
        self.key_a = dh.key_a # For testing
        self.key_b = dh.key_b # For testing
    
    def crack_bf(self): # Cracking DH protocol using bruteforce (not effective)
        timer = u.Timer("bruteforce")
        for pri_a in range(1, self.prime-1):
            tested_pub_a = pow(self.generator, pri_a, self.prime)
            if tested_pub_a == self.pub_a:
                timer.stop(pow(self.pub_b, pri_a, self.prime), self.key_a)
                return True

    def crack_bsgs(self): # Cracking DH protocol using baby-step giant-step algorithm
        timer = u.Timer("Baby-Step Giant-Step")
        pri_b = self.bsgs_algorithm(self.generator, self.prime, self.pub_b)
        if pri_b is None:
            print("Cracking failed")
            return
        timer.stop(pow(self.pub_a, pri_b, self.prime), self.key_b)

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
