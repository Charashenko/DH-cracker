import dhprotocol as dhp

for i in range(2, 40):
    dh_protocol = dhp.DiffieHellman(i)
    print(dh_protocol)
