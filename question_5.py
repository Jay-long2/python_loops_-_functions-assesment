def print_even_value_keys(input_dict):
    # Iterate through the dictionary
    for key, value in input_dict.items():
        # Check if the value is an even number
        if isinstance(value, int) and value % 2 == 0:
            print(key)

# Example usage
example_dict = {'a': 2, 'b': 3, 'c': 4}
print_even_value_keys(example_dict)
