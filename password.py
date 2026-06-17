import random
import string

def password_creator():
    print("Welcome to the Random Password Creator!")

    try:
        size = int(input("How long should the password be? "))
        if size < 1:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("That’s not a valid number. Please try again.")
        return

    # Define character set: letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation

    # Build the password
    password = ''.join(random.choices(characters, k=size))

    print("\nYour new password is:\n" + password)

# Start the generator
password_creator()
