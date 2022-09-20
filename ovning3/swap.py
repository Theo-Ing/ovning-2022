def swap(name):
    # name = "xxxx xxxxxx"

    # Hitta mellanrummet
    for i in range(len(name)):
        if name[i] == " ":
            break

    # Byt plats
    last = name[i+1:]
    first = name[:i]
    swapped = last + " " + first
    return swapped

def main():
    name = input("Name: ")
    result = swap(name)
    print("Swapped name:", result)

main()
