import random
import string

print("=== Secure Password Generator ===")

length = int(input("Enter password length: "))

# Ensure minimum length
if length < 4:
    print("Password length should be at least 4")
else:
    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill remaining length
    all_chars = letters + digits + symbols
    for i in range(length - 3):
        password.append(random.choice(all_chars))

    # Shuffle to make it random
    random.shuffle(password)

    # Convert list to string
    final_password = "".join(password)

    print("Generated Secure Password:", final_password)
