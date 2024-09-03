import random
import string

def generate_password(length=12, use_special_chars=True):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine all character sets
    all_characters = letters + digits + special_chars
    
    # Check if the password length is valid
    if length < 1:
        raise ValueError("Password length must be at least 1 character.")
    
    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    # User input for password length and special characters
    try:
        length = int(input("Enter the desired password length: "))
        use_special_chars = input("Include special characters? (yes/no): ").lower() in ['yes', 'y']
        
        # Generate and display the password
        password = generate_password(length, use_special_chars)
        print(f"Generated Password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
