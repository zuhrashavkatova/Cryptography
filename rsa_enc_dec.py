# 🔑 Asymmetric Encryption → RSA (Rivest-Shamir-Adleman) 1977 year


from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os

# 🔑 Kalitlar yaratish
def generate_keys():
    if not os.path.exists("private_key.pem"):
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()

        with open("private_key.pem", "wb") as f:
            f.write(private_key.private_bytes(
                serialization.Encoding.PEM,
                serialization.PrivateFormat.PKCS8,
                serialization.NoEncryption()
            ))

        with open("public_key.pem", "wb") as f:
            f.write(public_key.public_bytes(
                serialization.Encoding.PEM,
                serialization.PublicFormat.SubjectPublicKeyInfo
            ))

# 🔒 Shifrlash
def encrypt_message(message):
    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(), label=None)
    )
    return encrypted

# 🔓 Tiklash
def decrypt_message(encrypted):
    with open("private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    decrypted = private_key.decrypt(
        encrypted,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(), label=None)
    )
    return decrypted.decode()

# 👇 Foydalanuvchi interfeysi
if __name__ == "__main__":
    print("🔑 RSA Encryption/Decryption")

    generate_keys()

    user_input = input("✍️  Matn kiriting: ")
    encrypted = encrypt_message(user_input)
    print(f"🔐 Shifrlangan: {encrypted}")

    decrypt_now = input("🔓 Tiklamoqchimisiz? (yes/no): ")
    if decrypt_now.lower() == 'yes':
        decrypted = decrypt_message(encrypted)
        print(f"📬 Tiklangan matn: {decrypted}")
