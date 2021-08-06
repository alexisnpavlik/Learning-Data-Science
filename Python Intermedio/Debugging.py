def divisors(number):
    divisors=[]
    for i in range(1,number+1):
        if number%i==0:
            divisors.append(i)
    return divisors     

def run():
    number=int(input("Numero  "))
    print(divisors(number))
    print("fin de ejecucuion")

if __name__=='__main__':
    run()