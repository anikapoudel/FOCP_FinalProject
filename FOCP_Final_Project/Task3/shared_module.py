import codecs

def read_password_file(filename):
    with open(filename, 'r') as passwd_file:
        lines = passwd_file.readlines()
    return lines

def write_password_file(filename, lines):
    with open(filename, 'w') as passwd_file:
        passwd_file.writelines(lines)

def find_user_by_username(lines, username):
    for line in lines:
        fields = line.strip().split(':')
        if fields[0] == username:
            return line
    return None

def encrypt_password(password):
    return ''.join([chr((ord(char) - ord('a') + 13) % 26 + ord('a')) if 'a' <= char <= 'z' else char for char in password])

