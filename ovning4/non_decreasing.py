def non_dec(lst):
    if len(lst) == 1:
        return True
    else:
        if lst[0] > lst[1]:
            return False
        else:
            return non_dec(lst[1:])
        # Also works: return (lst[0] <= lst[1]) and non_dec(lst[1:])

# assert testar om påståndet är "sant", om inte ger den Error, bra sätt att testa kod
assert non_dec([1, -1, 3]) == False
assert non_dec([-1, 1, 2, 2, 5])