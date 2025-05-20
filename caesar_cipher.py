# # 🔐 Caesar cipher (Gaius Julius Caesar) Sezar shifriga Yuliy Sezar nomi berilgan
# # U alifbodan foydalangan, bunda shifrni ochish uchta harfni chapga siljitadi.

# # 🔑 encryption
# text = "hello"
# shift = 3
# ciphertext = 'khoor'
# def caesar_enc(plaintext, shift):
#     result = ""
#     for i in plaintext:
#         if i.isalpha():
#             if i.islower():
#                 num = ord(i) + shift
#                 if num > ord('z'):
#                     num -= 26
#             elif i.isupper():
#                 num = ord(i) + shift
#                 if num > ord('Z'):
#                     num -= 26
#             result += chr(num)
#         else:
#             result += i
#     print(result)     

# # 🔓Decryption
# def ceaser_dec(ciphertext, shift):
#     result = ""
#     for i in ciphertext:
#         if i.isalpha():
#             if i.islower():
#                 num = ord(i) - shift
#                 if num > ord('z'):
#                     num -= 26
#             elif i.isupper():
#                 num = ord(i) - shift
#                 if num > ord('Z'):
#                     num -= 26
#             result += chr(num)
#         else:
#             result += i
#     print(result)                       

# caesar_enc(text, shift)
# ceaser_dec(ciphertext, shift)


# 🔑 encryption
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

print(caesar_encrypt("HELLO", 3))

# 🔓Decryption
def caesar_decrypt_all(cipher_text):
    for shift in range(26):
        decrypted = ""
        for char in cipher_text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                decrypted += chr((ord(char) - base - shift) % 26 + base)
            else:
                decrypted += char
        print(f"Shift {shift}: {decrypted}")

caesar_decrypt_all("KHOOR")




