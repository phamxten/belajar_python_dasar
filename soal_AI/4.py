user = input("Masukkan kalimat yang ingin dicari: ")

for spasi in user:
    if spasi == " ":
        print("Terdapat spasi dalam input")
        break
else:
    print("Tidak terdapat spasi dalam input")
