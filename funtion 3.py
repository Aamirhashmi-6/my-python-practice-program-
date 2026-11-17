def multiply_list(numbers):
    result = 1
    for num in numbers:
        result = result * num

    return result

my_list = [1,2,3,4,5,]
print(multiply_list(my_list))
