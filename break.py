win = 17

while True:
    tebak = int(input("Tebakan Anda (1-20): "))

    if tebak == win:
        print("Selamat, tebakan benar!")
        break
    else:
        print("Tebakan salah, coba lagi!")
    