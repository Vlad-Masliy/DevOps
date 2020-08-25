def euler_1():
    euler = []
    for i in range(1, 100000001):
        if i % 3 == 0 or i % 5 == 0:
            euler.append(i)
    return sum(euler)


print(euler_1())
