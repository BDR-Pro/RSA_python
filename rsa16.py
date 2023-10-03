import random
import sympy

def generate_keypair(bits):
    p = sympy.randprime(2 ** (bits - 1), 2 ** bits)
    q = sympy.randprime(2 ** (bits - 1), 2 ** bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # Commonly used public exponent
    d = sympy.mod_inverse(e, phi)

    public_key = (n, e)  # Store (n, e) as the public key
    private_key = (n, d)  # Store (n, d) as the private key

    return public_key, private_key

def encrypt(public_key, plaintext):
    n, e = public_key
    encrypted_msg = pow(plaintext, e, n)
    return encrypted_msg

def decrypt(private_key, ciphertext):
    n, d = private_key
    decrypted_msg = pow(ciphertext, d, n)
    return decrypted_msg

# Example usage
public_key, private_key = generate_keypair(16)
message = 29201
ciphertext = encrypt(public_key, message)
decrypted_message = decrypt(private_key, ciphertext)
nbin=bin(public_key[0]).replace("0b", "")
print("Original Message:", message)
print("Public Key (n, e):", public_key)
print("Private Key (n, d):", private_key)
print("Ciphertext:", ciphertext)
print("Decrypted Message:", decrypted_message)
print("n of public key in binary:",nbin)
print("length of n:", len(nbin))
print("RSA keys generated")
