def sayHello():
    print("Hello")
sayHello()

def sayHello(name):
    print("Hello, " + name)
sayHello("Sana")
'''
Python does not support typical function overloading. Only the latest definition of the function remains valid. 
'''

def cube(num):
    return pow(num, 3)
print(cube(2))
