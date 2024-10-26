def num_size(num):
    sorted = list(num)
    sorted.sort()
    tuple_sort = tuple(sorted)
    print(tuple_sort[-1])
numbers = (10,20,45,67,32,54)
largest_number = num_size(numbers)

    