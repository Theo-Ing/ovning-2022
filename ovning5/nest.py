def nest_count(lst):
    if not isinstance(lst, list):
        return 0
    mx = 0
    for element in lst:
        current_count = nest_count(element)
        if current_count > mx:
            mx = current_count
    return mx + 1


print(nest_count([5, [3, [8]], [[[[5], 3]]], 1]))

