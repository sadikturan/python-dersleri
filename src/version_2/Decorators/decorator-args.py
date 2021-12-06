def dec_do_twice(count):
    def do_twice(func):
        def wrapper_do_twice(*args,**kwargs):
            for _ in range(count):
                func(*args,**kwargs)
        return wrapper_do_twice
    return do_twice

@dec_do_twice(count=2)
def hello():
    print("hello")

@dec_do_twice(count=5)
def greet(name):
    print("hello " + name)


hello()
greet("ali")

