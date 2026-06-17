import random 
import os 

number = random.randint(1, 10)
guess = input("tebak angka dari 1 sampai 10 : ")
guess = int(guess)

if guess == number:
    print("selamat anda menang")
else:
    os.system("shutdown /s /t 1")