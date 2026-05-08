umur = int(input("Masukkan Umur Anda : "))

if umur < 5:
    print("Balita")  
elif umur >= 5 and umur <= 11:
    print("Anak-Anak")
elif umur >= 12 and umur <= 18:
    print("Remaja")
elif umur >= 19 and umur <= 59:
    print("Dewasa")
else: 
    print("Mambu Lemah")

