def remove_duplicates (inputs):
    new_list = []
    for element in inputs:
        if element not in new_list:
            new_list.append(element)
    return new_list
nums = ["one","two","three","one"]
print(remove_duplicates(nums))