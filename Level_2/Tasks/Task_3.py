import string

def check_password_strength(password):
    has_upper = has_lower = has_digit = has_special = False
    
    for c in password:
        if c.isupper(): has_upper = True
        elif c.islower(): has_lower = True
        elif c.isdigit(): has_digit = True
        elif c in string.punctuation: has_special = True

    length_ok = len(password) >= 8

    if all([length_ok, has_upper, has_lower, has_digit, has_special]):
        return "Strong password"
    elif length_ok and ((has_upper and has_lower) or (has_digit and has_special)):
        return "Moderate password"
    else:
        return "Weak password"

password = input("Enter a password to check its strength: ")
print(check_password_strength(password))