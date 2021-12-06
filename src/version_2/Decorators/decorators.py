def selamlama(fn):
    def wrapper(ad):
        print("hoş geldiniz.")
        fn(ad)
        print("görüşmek üzere.")
    return wrapper

@selamlama
def gunaydin(ad):
    print("günaydın benim adım " + ad)

@selamlama
def iyigunler(ad):
    print("iyi günler benim adım " + ad)


# gunaydin("ahmet")
# iyigunler("yağmur")





