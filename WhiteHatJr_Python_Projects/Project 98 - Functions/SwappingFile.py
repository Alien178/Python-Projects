def swapFileData():
    file1 = input("Enter First File Name / Path:\n")
    with open(file1, "r") as a:
        data_a = a.read()

    file2 = input("Enter Second File Name / Path:\n")
    with open(file2, "r") as b:
        data_b = b.read()

    with open(file1, "w") as a:
        a.write(data_b)

    with open(file2, "w") as b:
        b.write(data_a)

swapFileData()