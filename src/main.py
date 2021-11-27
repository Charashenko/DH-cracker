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

dhprotocol = dhp.DiffieHellman(19) # Create DH key exchange with required bitlen
print(dhprotocol)
dhcracker = dhc.Cracker(dhprotocol)
dhcracker.crack_bf()
dhcracker.crack_bsgs()