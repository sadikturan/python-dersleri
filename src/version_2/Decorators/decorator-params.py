def do_twice(func):
    def wrapper_do_twice(*args,**kwargs):
        return func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper_do_twice

@do_twice
def hello():
    print("hello")

@do_twice
def greet(msg):
    print("hello " + msg)

@do_twice
def return_greeting(name):
    print("greeting function")
    return f"hello, {name}"

# hello()
# greet("world")
# return_greeting("ali")
print(return_greeting("ali"))