
user = input("Masukkan kata yang ingin dicari: ")
for kata in user:
    if kata.isupper():
        print("ada huruf besar dalam kalimat")
        break
else:
    print("tidak ada huruf besar dalam kalimat")
