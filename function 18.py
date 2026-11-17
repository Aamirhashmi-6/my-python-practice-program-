def largest(lst):
    big = lst[0]
    for i in lst:
        if i > big:
            big = i
    return big

print(largest([10, 20, 30, 40, 50]))
