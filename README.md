# Encrypt-a-password-in-Python
Encrypt Password in Python using the bcrypt

To encrypt a password in Python, it is recommended to use a secure hashing algorithm instead of encryption.

Encryption is a two-way process, and passwords should be stored in a way that they cannot be easily reversed. Hashing is a one-way process, making it more suitable for password storage.

Here’s an example using the bcrypt library, which is a popular choice for secure password hashing in Python. You can install it using:

Then, you can use it in your Python code like pws.py file or can  directly downlaod and run.

hash_password takes a password as input, generates a random salt, and hashes the password with the salt. check_password is used to check if a given password matches a stored hashed password.

Remember to store only the hashed password in your database, not the actual user password.

When a user tries to log in, you hash the entered password using the same salt and compare it to the stored hashed password.

Why We use bcrypt?

bcrypt is a good choice because it incorporates a salt and is computationally expensive, making it resistant to brute force and rainbow table attacks.


