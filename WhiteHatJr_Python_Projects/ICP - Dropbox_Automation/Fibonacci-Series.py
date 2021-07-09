nterms = int(input("How many terms?\n"))

n1, n2 = 0, 1

count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms,":")
else:
    print("Fibonacii Sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth

        count += 1