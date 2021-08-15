
def is_primer(integer:int)-> bool:
    divisors=[i for i in range(2,integer) if integer%i == 0]
    return len(divisors)==0
        

def run():
    print(is_primer("s"))

if __name__=='__main__':
    run()