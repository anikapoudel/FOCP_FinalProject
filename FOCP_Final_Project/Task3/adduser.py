import sys
from getpass import getpass
from shared_module import read_password_file, write_password_file, find_user_by_username, encrypt_password

def add_user():
    print("Namaste and Welcome new user!")
    username = input("Username: ")
    realname = input("Real Name: ")
    password = getpass("Password (hidden): ")

    # Read existing users
    user_data = read_password_file('passwd.txt')

    # Check if user already exists
    if find_user_by_username(user_data, username) is not None:
        print("Oops! Username already taken. Try another one.")
        return

    # Encrypt password
    encrypted_pwd = encrypt_password(password)

    # Creating a new entry
    new_user = f'{username}:{realname}:{encrypted_pwd}\n'
    user_data.append(new_user)

    # Write the updated data back to file
    write_password_file('passwd.txt', user_data)
    print("Yay! New user added.")

if __name__ == "__main__":
    add_user()
