nama = "yanto"
umur = 15
pesan = "hai nama saya "+ nama + ",umur " + str(umur)
print(pesan)

print(len(nama))
print(len(pesan))

name = "santo"
print(name[0])  # s (huruf pertama)
print(name[1])  # a (huruf kedua)
print(name[2])  # n (huruf ketiga)
print(name[3])  # t (huruf keempat)
print("batas")
print(name[-1]) # o (huruf terakhir)
print(name[-2]) # t (huruf keempat)
print(name[-3]) # n (huruf ketiga)
print("batas")
print(name[1:4]) # ant (huruf 2-4)
print(name[0:3]) # san (huruf 1-3)
print(name[2:5]) # nto (huruf 3-5)
print("batas")
print(name[:4]) #sant (huruf 1-4)
print(name[1:]) #anto (huruf 2-5)
print(name[:]) #anto (huruf 1-5) default

nama = "kicau mania"
print(nama)
nama_upper = nama.upper()
print(nama_upper)
nama_lower = nama.lower()
print(nama_lower)

nama = "joko samudro"
print(nama)
nama_tittle = nama.title()
print(nama_tittle)
nama_capitalize = nama.capitalize()
print(nama_capitalize)

nama = "     joko     "
nama_strip = nama.strip()
print(nama_strip)

kalimat = "she love him"
kalimat_baru = kalimat.replace("him", "ME")
print(kalimat_baru)

contoh = "she is love my friend"
contoh_baru = contoh.replace("my friend", "me")
print(contoh_baru)

nama = "bambang sugi prasojo"
jumlah_huruf = nama.count("pras")
print(jumlah_huruf)

kalimat = "visual studio code is the best"
posisi = kalimat.find("studio")
print(posisi)


kalimat = "Baris Pertama\nBaris Kedua"
print(kalimat)

kalimat = "Nama:\tJoko Sembung\nUmur:\t23"
print(kalimat)

Lokasi = "C:\\User\\Vann\\Document"
print(Lokasi)

kalimat = "She say \"Hello\" "
print(kalimat)

nama = "Leni Mbok Sekaradi"
umur = 37
asal = "Jawir"

print(f"hai perkenal kan nama saya {nama} umur saya {umur} asal saya {asal}")

harga = 500000
jumlah = 3
total = f"Total dari barang yang kamu beli adalah {harga * jumlah:,}"
print(total)

nama = "eko junaidi"
kalimat = f"hai {nama.capitalize()}"
print(kalimat)