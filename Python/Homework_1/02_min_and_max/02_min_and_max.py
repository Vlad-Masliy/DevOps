numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
new_numbers = []

for i in numbers:
    try:
        new_numbers.append(int(i))
    except ValueError:
        print('ValueError element', i, 'could not transform in int')
        continue
    except TypeError:
        print('TypeError element', i, 'could not transform in int')
        continue
numbers = new_numbers

print(min(numbers))
print(max(numbers))
