def even():
    lst = []
    for i in range(100, 151):
        if i % 2 == 0:
            lst.append(i)
    return lst

print(even())
