import dhprotocol as dhp
import dhcracker as dhc

def getMethods():
    return {
            1: "dhcrack.crack_bf()",
            2: "dhcrack.crack_bsgs()"
        }

def solveDH(bitlen, method):
    dhprot = dhp.DiffieHellman(bitlen) # Create DH key exchange with required bitlen
    dhcrack = dhc.Cracker(dhprot) # Create DH Cracker
    try:
        exec(getMethods()[method], {"dhcrack": dhcrack}) # Execute one of the methods
        return dhcrack
    except KeyboardInterrupt:
        print("\nCracking was cancelled by the user...")
    
def consoleApp():
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

    cont = "y"
    while cont == "y":
        bitlen = 0
        while bitlen <= 1:
            bitlen = int(input("Choose a bit length of a prime number (2-x): "))

        method = 0
        while method not in getMethods():
            method = int(input("Choose method of cracking:\n1 = Bruteforce,\n2 = Baby-step Giant-step\n"))

        results = solveDH(bitlen, method)
        if results:
            print("#####  Results of cracking  #####")
            for key, value in results.getResults().items():
                print(f"{key} > {value}")

        cont = input("Do you wish to continue? [y/N] ")
        if cont.lower() not in ["y", "yes"]:
            cont = "n"

if __name__ == "__main__":
    consoleApp()