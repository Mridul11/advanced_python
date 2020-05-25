import sys 

class Gen:
    def __init__(self, n):
        super().__init__()
        self.n = n 
        self.last = 0 

    def __next__(self):
        return self.next()


    def next(self):
        if self.last == self.n:
            raise StopIteration() 
            
        rv = self.last ** 2 
        self.last += 1 
        return rv 


g = Gen(100)

while(True):
    try:
        print(next(g))
    except StopIteration:
        break 


def gen(n):
    for i in range(n):
        yield i ** 2 

x = [i **2 for i in range(10000)]

g = gen(1000)
print("===================")
print(sys.getsizeof(x))
print(sys.getsizeof(g))

# for i in g:
#     print(i)