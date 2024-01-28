import sys
from getpass import getpass
from shared_module import read_password_file, write_password_file, find_user_by_username, encrypt_password

def passwd():
    username = input("Enter username: ")

    lines = read_password_file('passwd.txt')

    # Find the user by username
    user_line = find_user_by_username(lines, username)
    if user_line is None:
        print("User not found. No change made.")
        return

    # Get the current password and verify it
    current_password = getpass("Current Password: ")
    _, _, stored_password = user_line.strip().split(':')
    if encrypt_password(current_password) != stored_password:
        print("Invalid current password. No change made.")
        return

    # Get and confirm the new password
    new_password = getpass("New Password: ")
    confirm_password = getpass("Confirm: ")
    if new_password != confirm_password:
        print("Passwords do not match. No change made.")
        return

    # Update the password
    updated_line = f'{username}:{encrypt_password(new_password)}\n'
    lines[lines.index(user_line)] = updated_line

    write_password_file('passwd.txt', lines)
    print("Password changed.")

if __name__ == "__main__":
    passwd()
