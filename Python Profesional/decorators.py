from datetime import datetime

def time_execute(func):
    def timer():
        inicial_time=datetime.now()
        func()
        absolute_time=f"Pasaron {(datetime.now()-inicial_time).total_seconds()} segundos"
        return absolute_time
    return timer

@time_execute
def suma():
    for i in range(1,100):
        print(i+i**2)

print(suma())

