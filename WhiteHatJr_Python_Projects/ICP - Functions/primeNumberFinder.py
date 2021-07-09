num = int(input("Please Enter a Number!\n"))

for j in range(2, num + 1):
    prime = True
    if j > 1:
        for i in range(2, j):
            if (j % i == 0):
                prime = False
        if prime:
            print(j)



            