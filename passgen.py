import random
import string

def generate_password(length):
    """Generate a random password of the given length"""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    num_passwords = 100
    min_length = 12
    max_length = 20

    passwords = []
    for _ in range(num_passwords):
        length = random.randint(min_length, max_length)
        password = generate_password(length)
        passwords.append(password)

    with open('passwords.txt', 'w') as f:
        for i, password in enumerate(passwords):
            f.write(f'Password {i+1}: {password}\n')

if __name__ == '__main__':
    main()
