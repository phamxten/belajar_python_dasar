password_benar = "12345"

for i in range(3):
    password = input("Masukkan password: ")
    
    if password == password_benar:
        print("login berhasil")
        break
else:
    print("akun terkunci")