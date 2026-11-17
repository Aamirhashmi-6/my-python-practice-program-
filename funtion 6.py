def check_range(num, start, end):
    if num >= start and num <= end:
        return True
    else:
        return False

number = 15
print(check_range(number, 10, 20))
