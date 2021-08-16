# def main():
#     a=1

#     def nested():
#         print(a)

#     return nested()

# my_funt=main()
# del(main) #Se usa para elminar una funcion

# my_funt #nested recuerda "a" aunque se elimine "main" 


def make_multiplier(x):

    def multiplier(n):
        return x*n
    
    return multiplier

time10=make_multiplier(10)
time5=make_multiplier(5)

print(time10(5))
print(time5(8))