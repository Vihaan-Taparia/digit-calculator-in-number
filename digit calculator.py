def count_digits(input_string):
    digit_count = 0
    for char in input_string:
        if char.isdigit():
            digit_count += 1
    return digit_count

# Get input from the user
user_input = input("Please enter a number: ")

# Calculate the number of digits
num_digits = count_digits(user_input)

# Display the result
print(f"The number of digits in the given number is: {num_digits}")
