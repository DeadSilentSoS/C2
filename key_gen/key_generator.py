from cryptography.fernet import Fernet

# Generate a new random key
key = Fernet.generate_key()

# Save the key to a file (or another secure storage method)
key_filename = "encryption_key.key"  # Choose a secure file name
with open(key_filename, "wb") as key_file:
    key_file.write(key)

print("Encryption key generated and saved securely to", key_filename)
