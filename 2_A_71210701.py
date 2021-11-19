print ("#"*28)
print ("Kalkulator Advance Sederhana")
print ("#"*28)
print ("1. Menghitung sisa hasil bagi")
print ("2. Membulatkan ke bawah hasil pembagian")
print ("3. Mencari akar kubik sebuah bilangan")
menu= float(input("Masukkan menu yang anda pilih: "))
if menu == 1:
    dibagi= float(input("Masukkan bilangan yang ingin dibagi: "))
    pembagi= float(input("Masukkan bilangan pembagi: "))
    t1= float(dibagi % pembagi)
    print("Sisa hasil bagi", dibagi, "dibagi dengan", pembagi, "adalah", t1)
elif menu == 2:
    dibagi = float(input("Masukkan bilangan yang ingin dibagi: "))
    pembagi = float(input("Masukkan bilangan pembagi: "))
    t2 = float(int(dibagi / pembagi))
    print("Hasil pembagian", dibagi, "dibagi dengan", pembagi, "dibulatkan kebawah adalah", t2)
elif menu == 3:
    kubik = float(input("Masukkan bilangan yang ingin dicari akar kubiknya: "))
    t3 = float(kubik **(1/3))
    print("Akar kubik dari",kubik, "adalah", t3)
else:
    print("Menu yang anda pilih tidak tersedia")