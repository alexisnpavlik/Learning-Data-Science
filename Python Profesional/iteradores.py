
my_list = [1,2,3,4,5,6,7,8]
my_iter=iter(my_list)

while True:
    try:
        element=next(my_iter)
        print(element)
    except StopIteration:
        break

 