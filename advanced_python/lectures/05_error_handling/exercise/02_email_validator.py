############################## 02_email_validator ##############################
  ############################## TASK CONDITION ##############################
"""
 
"""

ALLOWED_DOMAINS = [".com", ".bg", ".org", ".net"]
MIN_USERNAME_LENGTH = 4

def name_too_short_error():
    raise ValueError("Name must be more than 4 characters")

def must_contain_at_symbol_error():
    raise ValueError("Email must contain @")

def invalid_domain_error():
    raise ValueError(f"Domain must be one of the following: {', '.join(ALLOWED_DOMAINS)}")

def validate_email(email_address):
    while email_address:
        try:
            if "@" not in email_address:
                must_contain_at_symbol_error()

            username, domain = email_address.split("@")

            if len(username) <= MIN_USERNAME_LENGTH:
                name_too_short_error()

            for d in ALLOWED_DOMAINS:
                if domain.endswith(d):
                    break
            else:
                invalid_domain_error()

            print("Email is valid")
        except ValueError as e:
            print(e)

        email_address = input()

validate_email(input())

