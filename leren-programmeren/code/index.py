import random
import string

def generate_password(length, use_numbers=True, use_symbols=True):
    # Define character sets for generating the password
    characters = string.ascii_letters  # Letters (both uppercase and lowercase)

    if use_numbers:
        characters += string.digits  # Numbers

    if use_symbols:
        characters += string.punctuation  # Symbols

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        include_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
        include_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

        generated_password = generate_password(password_length, include_numbers, include_symbols)
        print("Generated Password:", generated_password)
    except ValueError:
        print("Please enter a valid password length (an integer).") 