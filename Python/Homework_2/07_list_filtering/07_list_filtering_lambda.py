l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
l1 = list(filter(lambda i: type(i) == int, l))

print(l1)
