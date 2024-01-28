import sys
from getpass import getpass
from shared_module import read_password_file, find_user_by_username, encrypt_password

def login():
    username = input("User: ")
    password = getpass("Password: ")

    lines = read_password_file('passwd.txt')

    # Find the user by username
    user_line = find_user_by_username(lines, username)
    if user_line is None:
        print(f"User '{username}' not found.")
        return

    # Get and verify the password
    _, _, stored_password = user_line.strip().split(':')
    if encrypt_password(password) == stored_password:
        print(f"Access granted for '{username}'.")
    else:
        print("Access denied.")

if __name__ == "__main__":
    login()
