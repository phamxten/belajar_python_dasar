kata = input("Masukkan kata: ")
huruf_dicari = input("Masukkan huruf yang mau dicari: ")

for huruf in kata:
    if huruf == huruf_dicari:
        print("huruf" , huruf_dicari, "ditemukan")
        break
else:
    print("huruf", huruf_dicari, "tidak ditemukan")