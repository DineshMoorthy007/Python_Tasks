def is_valid_email(email):
    if "@" not in email or email.count("@") != 1:
        return False
    
    local_part, domain_part = email.split("@")

    if not local_part or not domain_part:
        return False
    if "." not in domain_part:
        return False
    if domain_part.startswith(".") or domain_part.endswith("."):
        return False

    return True

email_input = input("Enter an email address: ")
if is_valid_email(email_input):
    print("Valid email address.")
else:
    print("Invalid email address.")
