artikel= input("Masukkan artikel yang ingin dipindai: ")
kf= input("Masukkan nama klub fsvorit anda: ")
skor= input("Masukkan skor yang ingin dicari: ")

if kf+artikel and skor+artikel:
    print("Hasil pencarian ditemukan")
elif kf+artikel:
    print("Hanya", kf, "yang ditemukan pada artikel ini")
elif skor+artikel:
    print("Hanya skor", skor, "yang ditemukan pada artikel ini")
else:
    print("Hasil pencarian", kf,"dan", skor,"tidak ditemukan")