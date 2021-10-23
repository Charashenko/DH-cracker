import dhprotocol as dhp
import dhcracker as dhc

for i in range(2, 50): # bit range
    dhprotocol = dhp.DiffieHellman(i)
    print(dhprotocol)
    dhcracker = dhc.Cracker(dhprotocol)
    dhcracker.crack_bf()
