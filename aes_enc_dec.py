# 🔐 Symmetric Encryption → AES (Advanced Encryption Standard)


from cryptography.fernet import Fernet

# 🔑 Kalit yaratish
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# 🔑 Kalitni o'qish
def load_key():
    return open("secret.key", "rb").read()

# 🔒 Shifrlash
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(message.encode())

# 🔓 Tiklash
def decrypt_message(encrypted_msg):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_msg).decode()

# Foydalanuvchi interfeysi
if __name__ == "__main__":
    print("🔐 AES Encryption/Dekription")
    
    try:
        generate_key()
    except:
        pass

    user_input = input("✍️  Matn kiriting: ")
    encrypted = encrypt_message(user_input)
    print(f"🔒 Shifrlangan: {encrypted.decode()}")

    decrypt_now = input("🔓 Tiklamoqchimisiz? (yes/no): ")
    if decrypt_now.lower() == 'yes':
        decrypted = decrypt_message(encrypted)
        print(f"📩 Tiklangan matn: {decrypted}")



