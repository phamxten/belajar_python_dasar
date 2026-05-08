belanja_a = input("Masukkan jumlah belanjaan : ")
belanja_b = input("Masukkan jumlah belanjaan : ")
member = input("Apakah anda member? (ya/tidak) : ")

belanja_a = belanja_a.replace(",", "")
belanja_b = belanja_b.replace(",", "")

belanja_a = int(belanja_a)
belanja_b = int(belanja_b)

total = belanja_a + belanja_b 

if total > 100000:
        if member == "ya":
            diskon = total * 20/100
            total_bayar = total - diskon
            print(f"Total belanjaan anda adalah: Rp {int(total_bayar):,}".replace("," , ","))
            print("Anda mendapatkan diskon 20% karena anda member")
        if member == "tidak":
            diskon = total * 10/100
            total_bayar = total - diskon
            print("Total belanjaan anda adalah:", total_bayar)
            print("Anda mendapatkan diskon 10% karena anda bukan member")
if total <= 100000:
     print("Tidak mendapat diskon")