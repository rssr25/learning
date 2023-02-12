def star(func):
    def inner(*args, **kwargs):
        print('*' * 15)
        func(*args, **kwargs)
        print('*' * 15)
    
    return inner


def percent(func):
    
    def inner(*args, **kwargs):
        print('%' * 15)
        func(*args, **kwargs)
        print('%' * 15)
    

    return inner


@percent
@star
def printer(msg, name):
    print(msg, name)

printer("Hello", "Rahul")


def performAddition(func):

    def inner(a, b):
        func(a, b)
    return inner

@performAddition
def add(a, b):
    print(a + b)

print(add(3, 4))
