def mean():
    numbers = input("Skriv alla tal, separera med mellanrum: ")
    number_list = numbers.split(" ")
    summa = 0
    for i in number_list:
        summa += int(i)
    print("Medelvärdet:", sum / len(number_list))

mean()
