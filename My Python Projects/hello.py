msg = "Hello world"
print(msg)
msg = "Aayush is great"
print(msg)
msg = "Minecraft"
print(msg)
v2 = "Epic Games = Fortnite"
v1 = "Mojang = Minecraft"
temp = v2
v2 = v1
v1 = temp
print(v2)
print(v1)
a = 1
b = 2
if a < b:
    print("a is less than b")
    print("a is definitely less than b")
print("Not sure if a is less than b")
c = 5
d = 4
if c < d:
    print("c is less than d")
else:
    print("c is NOT less than d")
    print("I don't think c is less than d")
print("outside the if block")
e = 7
f = 8
if e < f:
    print("e is less than f")
elif e == f:
    print("e is equal to f")
elif e > f + 10:
    print("e is greater than f by more than 10")
else:
    print("e is greater than f")
