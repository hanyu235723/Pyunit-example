
def gen():
    lst = range(5)
    for i in lst:
        yield i* i

for i in gen():
    print(i, end="")