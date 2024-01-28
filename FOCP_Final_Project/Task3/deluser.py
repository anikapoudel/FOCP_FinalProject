import sys
from shared_module import read_password_file, write_password_file, find_user_by_username

def deluser():
    username = input("Enter username: ")

    lines = read_password_file('passwd.txt')

    # Find and remove the user by username
    user_line = find_user_by_username(lines, username)
    if user_line is not None:
        lines.remove(user_line)
        write_password_file('passwd.txt', lines)
        print("User Deleted.")
    else:
        print("User not found. Nothing changed.")

if __name__ == "__main__":
    deluser()
