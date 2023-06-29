import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def crack_password(password):
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    while True:
        attempt = ''.join(random.choice(characters) for _ in range(len(password)))
        attempts += 1
        if attempt == password:
            return attempts

# Şifre oluşturma
password1 = generate_password(4)
password2 = generate_password(3)
password3 = generate_password(2)

print("Oluşturulan Şifreler:")
print("Şifre 1:", password1)
print("Şifre 2:", password2)
print("Şifre 3:", password3)

# Şifre kırma denemeleri
print("\nŞifre Kırma Denemeleri:")
print("Şifre 1 kırıldı mı?", "Evet" if crack_password(password1) else "Hayır")
print("Şifre 2 kırıldı mı?", "Evet" if crack_password(password2) else "Hayır")
print("Şifre 3 kırıldı mı?", "Evet" if crack_password(password3) else "Hayır")


print("Şifre 1: " + password1);
print("Şifre 2: " + password2);
print("Şifre 3: " + password3);