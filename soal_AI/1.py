password_benar = "admin123"

for i in range(3):
    password = input("Masukkan password: ")
    
    if password == password_benar:
        print("Login berhasil")
        break
else:
    print("Akun terkunci")