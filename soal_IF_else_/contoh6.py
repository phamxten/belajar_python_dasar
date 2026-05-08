# # hari = input("Masukkan nama hari : ").lower()

# # if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis" or hari == "jumat":
# #     print("Hari Kerja")
# # elif hari == "sabtu" or hari == "minggu":
# #     print("Hari Libur")
# # else:
# #     print("Nama hari tidak valid")

# hari = input("Masukkan Nama Hari : ").lower()

# match hari:
#     case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
#         print("Hari Kerja")
#     case "sabtu" | "minggu":
#         print("Hari Libur")
#     case _:
#         print("Nama hari tidak valid")




hari = input("Masukkan Nama Hari : ").lower()

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat" | "sabtu" :
        print("Hari Gym")
    case "minggu":
        print("Hari Libur")
    case _:
        print("Nama hari tidak valid")
        
        
        