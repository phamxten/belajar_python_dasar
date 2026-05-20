list = [1, 2, 3, 4, 5]

user = input("Masukkan angka yang ingin dicari: ")

for angka in list:
    if int(angka) ==int(user):
        print("Angka", user, "ditemukan")
        break
else:
    print("Angka", user, "tidak ditemukan")
