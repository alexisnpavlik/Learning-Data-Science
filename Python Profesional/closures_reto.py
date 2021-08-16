def make_division(n):
    assert type(n)==int #Solo integer
    def division(x):
        assert type(x)==int #Solo integer
        return x/n
    
    return division


division_by_3=make_division(3)
print (division_by_3(18))

division_by_5=make_division(5)
print (division_by_5(100))

division_by_18=make_division(18)
print (division_by_18(54))