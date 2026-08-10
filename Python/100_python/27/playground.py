
def sum(*args):
    result = 0
    for n in args:
        result += n
    print(result)

def calculate(**kwargs):
    for key,value in kwargs.items():
        print(key, value)

calculate(nombre='Alan', edad=23)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')

my_car = Car(make='Nissan', model='GT-R')
print(my_car.model)
 