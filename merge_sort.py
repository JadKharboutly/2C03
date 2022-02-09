a = [99,8,7,6,5,4,3,2,1]


def merge(b, c):
    i = 0
    x = 0
    new_list = []

    while (len(b) != 0 and len(c) != 0):
        if (b[i] < c[x]):
            new_list.append(b[i])
            b.pop(i)
        else:
            new_list.append(c[x])
            c.pop(x)

    if (len(b) != 0):
        new_list.extend(b)
        return new_list
    elif (len(c) != 0):
        new_list.extend(c)
        return new_list
    else:
        return


def sortList(a):
    if (len(a) == 0 or len(a) == 1):
        return a

    middle = int(len(a) / 2)
    leftSide = sortList(a[slice(middle)])
    rightSide = sortList(a[slice(middle, len(a))])
    return merge(leftSide, rightSide)


print(sortList(a))


