class Test:
    a = '1'
    b = '2'
    c = '3'


t = Test()
print(t.__dict__)
print(t.a + ',' + t.b + ',' + t.c)
attr = [a for a in dir(t) if not a.startswith('__')]
for a in attr:
    print(a, getattr(t, a))
