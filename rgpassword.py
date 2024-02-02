import random
import string

def generate_password(length=12):
    # Define characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password by selecting random characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Generate a random password with the default length of 12 characters
random_password = generate_password()
print("Random Password:", random_password)
