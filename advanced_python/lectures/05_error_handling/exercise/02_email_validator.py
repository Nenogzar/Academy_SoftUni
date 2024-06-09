############################## 02_email_validator ##############################
  ############################## TASK CONDITION ##############################
"""
 
"""

# ALLOWED_DOMAINS = [".com", ".bg", ".org", ".net"]
# MIN_USERNAME_LENGTH = 4
#
# def name_too_short_error():
#     raise ValueError("Name must be more than 4 characters")
#
# def must_contain_at_symbol_error():
#     raise ValueError("Email must contain @")
#
# def invalid_domain_error():
#     raise ValueError(f"Domain must be one of the following: {', '.join(ALLOWED_DOMAINS)}")
#
# def validate_email(email_address):
#     while email_address:
#         try:
#             if "@" not in email_address:
#                 must_contain_at_symbol_error()
#
#             username, domain = email_address.split("@")
#
#             if len(username) <= MIN_USERNAME_LENGTH:
#                 name_too_short_error()
#
#             for d in ALLOWED_DOMAINS:
#                 if domain.endswith(d):
#                     break
#             else:
#                 invalid_domain_error()
#
#             print("Email is valid")
#         except ValueError as e:
#             print(e)
#
#         email_address = input()
#
# validate_email(input())


############ whit tkinter ################

import tkinter as tk
from tkinter import messagebox

ALLOWED_DOMAINS = [".com", ".bg", ".org", ".net"]
MIN_USERNAME_LENGTH = 4

def name_too_short_error():
    raise ValueError("Name must be more than 4 characters")

def must_contain_at_symbol_error():
    raise ValueError("Email must contain @")

def invalid_domain_error():
    raise ValueError(f"Domain must be one of the following: {', '.join(ALLOWED_DOMAINS)}")

def validate_email(email_address):
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

        messagebox.showinfo("Validation", "Email is valid")
        status_label.config(text="Email is valid", fg="green")
        email_entry.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Validation Error", str(e))
        status_label.config(text=str(e), fg="red")

def on_submit():
    email_address = email_entry.get()
    validate_email(email_address)

def clear_input():
    email_entry.delete(0, tk.END)
    status_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Email Validator")

# Create and place the widgets
tk.Label(root, text="Enter email:").pack(pady=10)
email_entry = tk.Entry(root)
email_entry.pack(pady=5)
submit_button = tk.Button(root, text="Validate", command=on_submit)
submit_button.pack(pady=5)
clear_button = tk.Button(root, text="Clear", command=clear_input)
clear_button.pack(pady=5)
status_label = tk.Label(root, text="", pady=10)
status_label.pack()

# Run the application
root.mainloop()

