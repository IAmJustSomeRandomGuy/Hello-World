def mergesort(a):
    if len(a) == 1:
        return a

    x = mergesort(a[0:int(round(len(a) / 2))])
    y = mergesort(a[int(round(len(a) / 2)): len(a)])

    b = x + y
    for n in range(len(b)):
        if len(x) != 0 and len(y) != 0:
            if y[0] < x[0]:
                b[n] = y[0]
                y.pop(0)
            elif x[0] < y[0]:
                b[n] = x[0]
                x.pop(0)
            else:
                b[n] = y[0]
                y.pop(0)
        elif len(x) == 0:
            b[n] = y[0]
            y.pop(0)
        elif len(y) == 0:
            b[n] = x[0]
            x.pop(0)
    return b


a = [5, 6, 2, 4, 9, 8, 8, 7, 1]
print(mergesort(a))
