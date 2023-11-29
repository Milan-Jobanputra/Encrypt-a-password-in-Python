import bcrypt

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(input_password, hashed_password):
    # Check if the input password matches the hashed password
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)

# Example usage:
user_password = "my_secure_password"
hashed_password = hash_password(user_password)

# Print the hashed password (store this in your database)
print("Hashed Password:", hashed_password)

# Check if a login password is correct
input_password = "my_secure_password"
if check_password(input_password, hashed_password):
    print("Password is correct!")
else:
    print("Password is incorrect.")