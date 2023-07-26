from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


#Use AES-256 to encrypt and decrypt a secret message created by the user.


def pad(s):
    # This function adds padding to your message, since AES data must be a multiple of 16 in length.
    return s + ((16 - len(s) % 16) * b'{')

def encrypt(plain_text, key):
    # Generates a random 16-byte IV.
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(pad(plain_text))

def decrypt(cipher_text, key):
    iv = cipher_text[:16]  # The first 16 bytes are the IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypted text might still have padding, which should be stripped.
    return cipher.decrypt(cipher_text[16:]).decode("utf-8").rstrip('{')

# Create a 256 bit (32 bytes) key.
key = get_random_bytes(32)

# Get message from user
message = input("Type a message to encrypt and decrypt: ")

# Encrypt the message
encrypted = encrypt(message.encode("utf-8"), key)
print(f"Encrypted message: {encrypted}")

# Decrypt the message
decrypted = decrypt(encrypted, key)
print(f"Decrypted message: {decrypted}")
