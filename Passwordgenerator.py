import random
import string

def generate_password(length):
    """
    Generate a strong and random password of the specified length.
    The password includes a combination of uppercase letters, lowercase letters,
    digits, and special characters.

    Parameters:
        length (int): The desired length of the password.

    Returns:
        str: The generated password.
    """
    if length < 4:
        print("Password length should be at least 4 for better security.")
        return None

    # Define character pools for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character pools
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password contains at least one character from each pool
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Add random characters to meet the desired length
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to randomize the order of characters
    random.shuffle(password)

    return ''.join(password)

def main():
    """
    Main function to prompt user input and generate the password.
    """
    print("Welcome to the Password Generator!")

    # Prompt the user to specify the desired password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 4:
                print("Password length should be at least 4. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    if password:
        print(f"\nGenerated Password: {password}")
        print("Keep it secure and don't share it with anyone!")

if __name__ == "__main__":
    main()
