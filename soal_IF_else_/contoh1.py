suhu = int(input("Masukkan Suhu : "))
cuaca = input("Masukkan Cuaca Saat Ini : (Pagi/Siang/Malam) ")

if suhu >= 20 and cuaca == "Siang":
    print("Tambahkan AC Biar Dingin")

if suhu >= 20 and cuaca == "Pagi":
    print("Tambahkan AC Biar Dingin") 
else:
    print("Biarin")