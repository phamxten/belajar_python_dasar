list = [1, 2, 3, 4, 5,6,7,8,9,10]

for angka in list:
    if int(angka) % 2 != 0:
        print(angka , "ada angka ganjil")
        break
else:
    print("tidak ada angka ganjil")