def tuples_to_dict(tuple_list):
    result_dict = {}  # Initialize an empty dictionary
    for item in tuple_list:
        key, value = item  # Unpack each tuple into key and value
        result_dict[key] = value  # Add the key-value pair to the dictionary
    return result_dict

# Example usage
input_list = [("apple", 5), ("banana", 3), ("cherry", 7)]
output_dict = tuples_to_dict(input_list)
print(output_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}
