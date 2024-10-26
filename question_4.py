def string_converter(strings):
    reversed_list = []  # Initialize an empty list to store the reversed strings
    for s in strings:
        reversed_list.append(s[::-1])  # Reverse each string using slicing and add it to the new list
    return reversed_list  # Return
names = ["Mark","Joseph","Romeo","Theodor","Tariq"]
reversal = string_converter(names)
print(reversal)
