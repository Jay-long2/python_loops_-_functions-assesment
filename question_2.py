def get_user_input():
    while True:
        user_input = input("Enter a word (type 'exit' to stop): ")
        if user_input.lower() == "exit":  # Check if the input is 'exit'
            print("Exiting the loop. Goodbye!")
            break  # Exit the loop
        print(f"You entered: {user_input}")  # Print the user input

get_user_input()

