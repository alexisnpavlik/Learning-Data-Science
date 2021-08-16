from datetime import datetime

def time_execute(func):
    def timer():
        inicial_time=datetime.now()
        func()
        absolute_time=f"Pasaron {(datetime.now()-inicial_time).total_seconds()} segundos"
        return absolute_time
    return timer