class Foo(object):
    def show(self):
        print("Hi")

def add_attribute(self):
    print("Add attribtue!")


class Meta(type):
    def __new__(self, class_name, bases, attrs):
        a = {}
        for name, value  in attrs.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value

        # print(class_name)
        # print(bases)
        # print(attrs)
        print(a)
        return type(class_name, bases, a) 

    

class Dog(metaclass=Meta):
    x = 5 
    y = 10 

    def hello(self):
        print("Hi")

d = Dog()
print(d.x)

# Test = type('Test', (Foo,), { 'x': 11, 'add_attribute': add_attribute })
# t = Test()
# t.y = "Hey There!"
# print(t.x)
# print(t.y)
# t.add_attribute()
# t.show()