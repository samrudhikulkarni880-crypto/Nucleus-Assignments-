import random
import string

def generate_password(length):
    
    alphabets = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    all_chars = alphabets + digits + special

    password = ""

    for i in range(length):
        password += random.choice(all_chars)

    return password


def main():
    length = int(input("Enter password length: "))

    password = generate_password(length)

    print("Generated Password:", password)


if __name__ == "__main__":
    main()