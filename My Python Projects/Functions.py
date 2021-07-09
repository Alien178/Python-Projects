def function1():
    print("ahhhh")
    print("ahhhhh 2")
print("this is outside the function")
function1()
def function2(x):
    return 2*x
a = function2(3)
print(a)
def function3(x, y):
    return x + y
b = function3(30, 20)
print(b)
def function4(x):
    print(x)
    print("still in this function")
    return 3*x
c = function4(10)
print(c)
