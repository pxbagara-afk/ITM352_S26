import cryptography
from cryptography.fernet import Fernet
print(cryptography.__version__)
#This program checks and prints the version of the cryptography Library

key = Fernet.generate_key()
cipher_suite = Fernet(key)
encoded_text = cipher_suite.encrypt("This is a really secret message".encode('utf-8'))
print(f"Encoded text: {encoded_text}")

#Use the cryptography library to encode and decode a message
decoded_text = cipher_suite.decrypt(encoded_text)
print(f"Decoded text: {decoded_text.decode('utf-8')}")

