kata = input("Masukkan kata: ")
huruf_dicari = input("Masukkan huruf yang ingin dicari: ")

for huruf in kata:
    if huruf == huruf_dicari:
        print("Huruf", huruf_dicari, "ditemukan")
        break
else:
    print("Huruf", huruf_dicari, "tidak ditemukan")