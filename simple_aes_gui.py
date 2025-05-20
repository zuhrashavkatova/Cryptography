from tkinter import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt():
    key = key_entry.get().encode('utf-8')
    text = text_entry.get("1.0", END).strip().encode('utf-8')
    cipher = AES.new(pad(key, 16), AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(text, 16))
    result.set(base64.b64encode(encrypted).decode('utf-8'))

def decrypt():
    key = key_entry.get().encode('utf-8')
    cipher_text = result.get().encode('utf-8')
    cipher = AES.new(pad(key, 16), AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(base64.b64decode(cipher_text)), 16)
    text_entry.delete("1.0", END)
    text_entry.insert(END, decrypted.decode('utf-8'))

# GUI
root = Tk()
root.title("AES Shifrlash GUI")
root.geometry("400x400")

Label(root, text="Kalit (Key):").pack()
key_entry = Entry(root, width=40)
key_entry.pack()

Label(root, text="Matn:").pack()
text_entry = Text(root, height=5, width=40)
text_entry.pack()

Button(root, text="🔐 Shifrlash", command=encrypt).pack(pady=5)
Button(root, text="🔓 Ochish", command=decrypt).pack(pady=5)

result = StringVar()
Label(root, text="Natija (Base64):").pack()
Entry(root, textvariable=result, width=40).pack()

root.mainloop()
