x = 5

hak = 0
devam = 'e'

result = 5 < x < 10

# and

# True, True => True
# True, False => False


result = (x > 5) and (x < 10)  
result = (hak > 0) and (devam == 'e') 

# or

result = (x > 0) or (x % 2 == 0)

# True, False => True
# True, True => True
# False, False => False

# not

result = not(x > 0)

# x, 5-10 arasında olan bir çift sayı mı?

result = ((x>5) and (x<10)) and (x%2==0)

print(result)

