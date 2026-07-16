functions = [sum, min, max]

numbers = range(1, 11)
print(list(numbers))

function = [sum, min, max]
number_list = range(1, 11)
for func in function:
    print("Function: {}, Result: {}".format(
        func.__name__, func(number_list)))
