l = [1, [], 2, [-19, 700, 0, [90, 33, [18, 77, [0, ], -2], 11, 16], -100]]


def find_numbers(structured_list, source_list):
    for i in source_list:
        if isinstance(i, int):
            structured_list.append(i)
        else:
            find_numbers(structured_list, i)
    return structured_list


new_list = find_numbers(list(), l)
print('Max is', max(new_list))
print('Min is', min(new_list))
print('Average is', round(sum(new_list) / len(new_list), 1))
