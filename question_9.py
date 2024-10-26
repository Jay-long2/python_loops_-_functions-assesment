def tagert_checker(list_input, target_sum):
    elements = 0
    for value in list_input:
        elements += value
        if elements == target_sum:
            print(True)
        else:
            print(False)
my_list = [12,13,3,5,2]
tagert_sum = 28
tagert_checker(my_list,tagert_sum)