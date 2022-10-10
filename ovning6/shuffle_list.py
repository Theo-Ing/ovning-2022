import random as rn

def shuffle(lst):
    result = []
    for i in range(len(lst)):
        index = rn.randint(0, len(lst) - 1)
        element = lst.pop(index)
        result.append(element)
    return result

print(shuffle([k**2 for k in range(10)]))
