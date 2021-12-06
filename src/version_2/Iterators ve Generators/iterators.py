# iterable?

# iterator?

sayilar = [1,2,3,4,5]
s = "hello"

def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            sayi = next(iterator)
            func(sayi)
        except StopIteration:
            break

# my_for(sayilar, print)
# my_for(s, print)

def kareal(x):
    print(x*x)

my_for(sayilar, kareal)