def is_palindrome(value):

    value = str(value)
    return value == value[::-1]

input_value = input("Enter a number or string to check if it's a palindrome: ").lower()

if is_palindrome(input_value):
    print(f"{input_value} is a palindrome.")
else:
    print(f"{input_value} is not a palindrome.")
