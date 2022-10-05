def m(l):
    t=1
    for e in l:
        t=t*e
    print(t)

l=[int(e) for e in input().split(",") ]
m(l)

