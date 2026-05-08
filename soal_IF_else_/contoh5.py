pin = int(input("Masukkan Pin Anda : "))
tarik = int(input("Masukkan Jumlah Uang yang Ingin Ditarik : "))
saldo = 25000000
saldo = int(str(saldo).replace(",", ""))

if pin == 12345:
    if saldo >= tarik:
        saldo -= tarik
        print("Transaksi Berhasil")
        print(f"Saldo Anda Sekarang: Rp {int(saldo):,}".replace(",", ","))
    else:
        print("Saldo Anda Tidak Cukup")
else:
    print("Pin Salah")