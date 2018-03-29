print("first import")

def mymethod():
    print("Method")

class MyClass(object):
    def __init__(self):
        self.foo = MyClass2()
        
    def my_instance_method(self):
        print("Instance method")

class MyClass2(object):
    pass
