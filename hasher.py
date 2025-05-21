import hashlib

def hash_text(text, algorithm='sha256'):
    text = text.encode()
    
    if algorithm == 'md5':
        return hashlib.md5(text).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(text).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(text).hexdigest()
    else:
        raise ValueError("⚠️ Noto‘g‘ri algoritm tanlandi!")

if __name__ == "__main__":
    print("🔐 Hashing Tool")
    user_input = input("✍️ Matn kiriting: ")

    print("\n🔽 Hash natijalari:")
    print("MD5    :", hash_text(user_input, 'md5'))
    print("SHA1   :", hash_text(user_input, 'sha1'))
    print("SHA256 :", hash_text(user_input, 'sha256'))
