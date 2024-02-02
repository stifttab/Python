import random
import string

def generate_password(length=12, mark='@'):
    # Define characters for the password (excluding the specified mark character)
    characters = string.ascii_letters + string.digits + string.punctuation.replace(mark, '')

    # Calculate the maximum number of characters available for the random part
    max_random_length = max(length - 1, 0)

    # Determine the random part of the password
    random_part = ''.join(random.choice(characters) for _ in range(max_random_length))

    # Calculate the remaining space for the mark character
    remaining_length = length - len(random_part)

    # Insert the specified mark character at a random position within the random part
    position = random.randint(0, len(random_part))
    password = random_part[:position] + mark + random_part[position:]

    return password

# Generate a random password with the default length of 12 characters (including '@' as the mark)
random_password = generate_password()
print("Random Password:", random_password)
