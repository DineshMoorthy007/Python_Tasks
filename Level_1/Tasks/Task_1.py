def reverse_string(s):
    return ''.join(reversed(s))

try:
    user_input = input("Enter a string to reverse: ")
    print("Reversed string:", reverse_string(user_input))

except Exception as e:
    print("Please enter a valid string.")