l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
def filter_list(l):
    l1 = []
    for i in l:
        if type(i) == int:
            l1.append(i)
    return l1

print(filter_list(l))

