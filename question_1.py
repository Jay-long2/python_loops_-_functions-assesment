for num in range(1,51):
    #print(num)
    if num % 3:
        print("Fizz")
    elif num % 5:
        print("Buzz")
    elif num % 3 and num % 5:
        print("FizzBuzz")

