import random
import math
from sympy import isprime, mod_inverse

def generate_prime(bitsize):
    while True:
        p = random.getrandbits(bitsize)
        if isprime(p):
            return p

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def keygen(bitsize=512):
    p = generate_prime(bitsize // 2)
    q = generate_prime(bitsize // 2)
    n = p * q
    nsquare = n * n
    g = n + 1
    lambda_ = lcm(p-1, q-1)
    mu = mod_inverse(lambda_, n)
    return (n, g), (lambda_, mu)

def encrypt(public_key, plaintext):
    n, g = public_key
    nsquare = n * n
    r = random.randint(1, n-1)
    while math.gcd(r, n) != 1:
        r = random.randint(1, n-1)
    c = (pow(g, plaintext, nsquare) * pow(r, n, nsquare)) % nsquare
    return c

def decrypt(private_key, public_key, ciphertext):
    lambda_, mu = private_key
    n, g = public_key
    nsquare = n * n
    u = pow(ciphertext, lambda_, nsquare) - 1
    plaintext = ((u // n) * mu) % n
    return plaintext

def main():
    # Generate keys
    public_key, private_key = keygen(512)
    print("Public Key:", public_key)
    print("Private Key:", private_key)

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
