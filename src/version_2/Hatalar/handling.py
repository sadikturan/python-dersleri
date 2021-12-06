while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except (ZeroDivisionError,ValueError) as e:
        print('hata oluştu.')
        print(e)
    except Exception as e:
        print('bilinmeyen bir hata oluştu.')
        print(e)
    else:
        break
    finally:
        print('finally bloğu çalıştı.')
    