from time import sleep
from datetime import datetime

def myFunction(func):
    def wrapper(*args):
        start = datetime.now()
        res = func(*args)
        duration = datetime.now() - start
        with open("log.txt", "a") as f:
            text = "{} -{}({}) -{} \n ".format(start, func.__name__, *args, duration)
            f.write(text)
            f.close()
        return res
    return wrapper    

@myFunction
def bar(x):
    sleep(2)
    return x**2

bar(4)