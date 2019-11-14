def createArray():
    ui = input("Add To Array: \n")
    array = []

    while(ui != "e"):
        ui = input("Add To Array: \n")
        array.append(ui)
    print(array)

createArray()