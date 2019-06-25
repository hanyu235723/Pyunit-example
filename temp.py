

class A ():
    def __init__(self,name):
        print (name)
    def __call__(self, *args, **kwargs):
        print ("call")

class a(A):
    pass

l=["a",'b','c','d','f']
print(list(map(a,l)))


