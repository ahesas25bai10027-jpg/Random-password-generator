import secrets
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    all_characters = lower + upper + digits + special

    # Ensure at least one of each
    password = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    # Fill the rest of the password length
    password += [secrets.choice(all_characters) for _ in range(length - 4)]

    # Shuffle to avoid predictable sequences
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

# Example usage
print("Generated Password:", generate_password(12))
