import random, math

bitlen = int(input("bits p = "))
def isprime(prim):
    prime = True
    if(prim % 2 == 0):
        prime = False
    else:
        root = int(math.sqrt(prim)+1)
        for i in range(3,root,2):
         if(prim % i == 0):
            prime = False
    return prime
p = random.getrandbits(bitlen)
if (p % 2 == 0):
    p += 1
while(not isprime(p)):
    p += 2
print("p = "+ str(p))
g = random.randint(int(math.sqrt(p)), p-1) #toto je problem, ten generator je pekne naprd pocitat
print("g = "+ str(g))
sec_a = random.randint(1, p-1) #klice pres random
sec_b = random.randint(1, p-1) 
pub_a = g**sec_a % p #ustanoveni A, B
pub_b = g**sec_b % p 
final_a = pub_b ** sec_a % p #výpočet klice pro oba, jestli funguje jsou stejne
final_b = pub_a ** sec_b % p
print("tajne klice alice a bob: " + str(final_a) + ", " + str(final_b))



