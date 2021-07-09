a = [3, 10, -1]
a.append(1)
a.append("hello")
a.append([1, 2])
print(a)
a.pop()
print(a)
a.pop()
print(a)
print(a[0])
print(a[3])
a[0] = 100
print(a)
b = ["banana", "apple", "microsoft"]
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)