# angka = 1

# while angka <= 5:
#     print(angka)
#     angka += 1

password = input("Masukkan password: ")

while password != "12345":
    password = input("Masukkan password: ")
    if password != "12345":
        print("password salah")

print("password benar")