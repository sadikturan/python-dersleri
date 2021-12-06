
f = open("msg.txt")

print(f.read())
print(f.read())

f.seek(0)
print(f.readable())

# >>> f.seek(0)
# 0
# >>> f.read()
# 'hello world.\nevewv\nvwevwev\nffwefwf\negweg'
# >>> f.read()
# '\nyeni satır'
# >>> f.seek(5)
# 5
# >>> f.read()
# ' world.\nevewv\nvwevwev\nffwefwf\negweg\nyeni satır'
# >>> 
# >>> f.seek(0)
# 0
# >>> f.readline()
# 'birinci satır.\n'
# >>> f.readline()
# 'ikinci satır.\n'
# >>> f.readline()
# 'üçüncü satır.\n'
# >>> f.readline()
# 'dördüncü satır.\n'
# >>> f.readline()
# 'beşinci satır.'
# >>> f.readline()
# ''
# >>> f.seek(0)
# 0
# >>> f.readlines()
# ['birinci satır.\n', 'ikinci satır.\n', 'üçüncü satır.\n', 'dördüncü satır.\n', 'beşinci satır.']
# >>> f.seek(0)
# 0
# >>> satirlar = f.readlines()
# >>> satirlar
# ['birinci satır.\n', 'ikinci satır.\n', 'üçüncü satır.\n', 'dördüncü satır.\n', 'beşinci satır.']
# >>> satirlar[0]
# 'birinci satır.\n'
# >>> satirlar[2]
# 'üçüncü satır.\n'
# >>> f
# <_io.TextIOWrapper name='msg.txt' mode='r' encoding='UTF-8'>
# >>> f.closed
# False
# >>> f.close()
# >>> f.closed
# True
# >>> f.seek(0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file.
# >>> f.read()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file.