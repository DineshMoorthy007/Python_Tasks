def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

text = input("Enter a string: ")
print("Palindrome" if is_palindrome(text) else "Not a palindrome")