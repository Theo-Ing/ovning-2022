def perm(lst):
    if len(lst) == 1:
        return [lst]
    else:
        total_list = []
        for i in range(len(lst)):
            smaller_perms = perm(lst[:i] + lst[i+1:])
            for permutation in smaller_perms:
                total_list.append([lst[i]] + permutation)
        return total_list

print(len(perm([1, 2, 3, 4, 5, 6])))
