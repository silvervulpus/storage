def listing(*args):
    a = (args)
    list = []
    for i in a:
        list.append(i)
    print(list)
    print(len(list))
    return list
f = 3
g = 2
h = "itemish"
listing(f, g, h)

def lister(*args, **kwargs):
    a = (args, kwargs)
    list = []
    for i in a:
        list.append(i)
    print(list)
    print(len(list))
    return list
lister(f, g, h, k = 8, q = "another")