l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
l1 = [i for i in l if type(i) == int]
print(l1)