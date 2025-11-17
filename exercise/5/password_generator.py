# Pedro is developing a registration system and needs to generate secure passwords for users. He wants a program that creates random passwords with uppercase letters, lowercase letters, numbers, and special characters.

# Create a program that generates a random 12-character password containing at least one uppercase letter, one lowercase letter, one number, and one special character. Display the generated password.

import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters to include all character types.")
    
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Ensure the password contains at least one of each required character type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the rest of the password length with a mix of all character types
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the resulting password list to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

# Generate and display the password
generated_password = generate_password()
print(f"Generated password: {generated_password}")