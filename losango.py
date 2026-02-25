rows_input = input("Insert your rows: ")

if rows_input.isdigit():
    rows = int(rows_input)

    #Parte de cima
    for i in range(rows):
        for j in range(rows - i):
            print(" ", end= "")
        for j in range(2 * i + 1):
            print("*", end= "")
        print()

    #Parte de baixo
    for i in range(rows, -1, -1):
        for j in range(rows - i):
            print(end= " ")
        for j in range(2 * i + 1):
            print("*", end="")
        print()

else:
    print("Insert a valid rows.")








