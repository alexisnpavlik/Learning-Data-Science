def my_gen():

    print ("hello word")
    n=0
    yield n

    print ("hello second")
    n=1
    yield n

    print ("hello three")
    n=2
    yield n

a=my_gen()

print(next(a)) # 0
print(next(a)) # 1
print(next(a)) # 2
print(next(a)) #StopIteration

