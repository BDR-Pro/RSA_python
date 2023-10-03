from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Generate an RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=512,
    backend=default_backend()
)

# Serialize the private key to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Generate the corresponding public key
public_key = private_key.public_key()

# Serialize the public key to PEM format
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

public_pem=public_pem.decode()
private_pem=private_pem.decode()

# Remove the "-----BEGIN-----" and "-----END-----" lines
private_pem = private_pem.replace("-----BEGIN PRIVATE KEY-----", "").replace("-----END PRIVATE KEY-----", "")
public_pem = public_pem.replace("-----BEGIN PUBLIC KEY-----", "").replace("-----END PUBLIC KEY-----", "")

bytes_data = public_pem.encode('utf-8')

# Step 2: Convert each byte to binary and concatenate
bit_sequence = ''.join(format(byte, '08b') for byte in bytes_data)


print("Public key:\n%s" % public_pem)
print("Private key:\n%s" % private_pem)
print("Public key in binary:\n%s" % bit_sequence)
print("RSA keys generated")
