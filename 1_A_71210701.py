a = float(input( "Masukan nilai rata-rata UG anda: " ))
b = float(input( "Masukan nilai TTS anda: " ))
c = float(input( "Masukan nilai TAS anda: " ))
print("="*25)

N1= ( 0.7*a )
N2= ( 0.15*b )
N3= ( 0.15*c )
t= ( N1+N2+N3 )
print("Nilai anda: ", t)

if t >= 85:
    print ("Nilai huruf anda: A")
elif t >= 80:
    print ("Nilai huruf anda: A-")
elif t >= 75:
    print ("Nilai huruf anda: B+")
elif t >= 70:
    print ("Nilai huruf anda: B")
elif t >= 65:
    print ("Nilai huruf anda: B-")
elif t >= 60:
    print ("Nilai huruf anda: C+")
elif t >= 55:
    print ("Nilai huruf anda: C")
elif t >= 45:
    print ("Nilai huruf anda: D")
else:
    print ("Nilai huruf anda: E")