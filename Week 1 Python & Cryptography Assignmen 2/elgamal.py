import random
import math
from sympy import isprime

def generate_prime(bitsize):
    while True:
        p = random.getrandbits(bitsize)
        if isprime(p):
            return p

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_keys(bitsize=512):
    p = generate_prime(bitsize)
    g = random.randint(2, p - 1)
    x = random.randint(2, p - 2)
    h = pow(g, x, p)
    return (p, g, h), x

def encrypt(public_key, plaintext):
    p, g, h = public_key
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    s = pow(h, k, p)
    c2 = (plaintext * s) % p
    return c1, c2

def decrypt(private_key, public_key, ciphertext):
    p, g, h = public_key
    x = private_key
    c1, c2 = ciphertext
    s = pow(c1, x, p)
    plaintext = (c2 * mod_inverse(s, p)) % p
    return plaintext

def main():
    # Generate keys
    public_key, private_key = generate_keys(512)
    print("Public Key (p, g, h):", public_key)
    print("Private Key (x):", private_key)

    # Prompt the user for a message
    plaintext = int(input("Enter a message to encrypt (as an integer): "))
    print("Plaintext:", plaintext)

    # Encrypt the message
    ciphertext = encrypt(public_key, plaintext)
    print("Ciphertext:", ciphertext)

    # Decrypt the message
    decrypted_plaintext = decrypt(private_key, public_key, ciphertext)
    print("Decrypted Plaintext:", decrypted_plaintext)

if __name__ == "__main__":
    main()
