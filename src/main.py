import dhprotocol as dhp
import dhcracker as dhc

logo = """
 ▄▄▄▄▄▄  ▄▄   ▄▄    ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄   ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
█      ██  █ █  █  █       █   ▄  █ █       █       █   █ █ █       █   ▄  █  
█  ▄    █  █▄█  █  █       █  █ █ █ █   ▄   █       █   █▄█ █    ▄▄▄█  █ █ █  
█ █ █   █       █  █     ▄▄█   █▄▄█▄█  █▄█  █     ▄▄█      ▄█   █▄▄▄█   █▄▄█▄ 
█ █▄█   █   ▄   █  █    █  █    ▄▄  █       █    █  █     █▄█    ▄▄▄█    ▄▄  █
█       █  █ █  █  █    █▄▄█   █  █ █   ▄   █    █▄▄█    ▄  █   █▄▄▄█   █  █ █
█▄▄▄▄▄▄██▄▄█ █▄▄█  █▄▄▄▄▄▄▄█▄▄▄█  █▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█ █▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█
"""
print(logo)

bitlen = 0
while bitlen <= 1:
    bitlen = int(input("Choose bit lenght of a prime number (2-x): "))

choices = {
    1: "dhcrack.crack_bf()",
    2: "dhcrack.crack_bsgs()",
    3: "dhcrack.crack_pol_rho()"
}
method = 0
while method not in choices:
    method = int(input("Choose method of cracking:\n1 = Bruteforce,\n2 = Baby-step Giant-step,\n3 = Pollard Rho\n"))

dhprot = dhp.DiffieHellman(bitlen) # Create DH key exchange with required bitlen
print(dhprot)
dhcrack = dhc.Cracker(dhprot)
exec(choices[method], {"dhcrack": dhcrack})