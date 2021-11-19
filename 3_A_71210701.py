a= str(input("Mendatar/Menurun?: "))
if a == "Mendatar":
    b= int(input("Masukkan kolom: "))
    print("#"*b)
elif a == "Menurun":
    b = int(input("Masukkan baris: "))
    row="*\n"
    print(row*b)
else:
    print("Pola tidak dikenali")