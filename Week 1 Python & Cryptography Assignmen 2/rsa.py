import random
from sympy import isprime, mod_inverse

# Function to generate a large prime number
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

# Function to compute the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to generate RSA keys
def generate_keys(bits=1024):
    # Generate two large prime numbers
    p = generate_prime(bits)
    q = generate_prime(bits)

    # Calculate n and the Euler's totient function phi
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Calculate d, the modular inverse of e
    d = mod_inverse(e, phi)

    return (e, n), (d, n)

# Function to encrypt a message
def encrypt(message, public_key):
    e, n = public_key
    # Convert the message to an integer and encrypt it
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt a message
def decrypt(encrypted_message, private_key):
    d, n = private_key
    # Decrypt each integer back to a character and join them to form the message
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Main function
def main():
    public_key, private_key = generate_keys(512)
    print("Public Key: ", public_key)
    print("Private Key: ", private_key)

    message = input("Enter the message to encrypt: ")
    print("Original Message: ", message)

    encrypted_message = encrypt(message, public_key)
    print("Encrypted Message: ", encrypted_message)

    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted Message: ", decrypted_message)

if __name__ == "__main__":
    main()
