print("=======================================")
print("Aplikasi untuk menghitung nilai mahasiswa")
input("Masukkan Nama Anda :")
input("Kelas : ")
print("=======================================")

nilai = int(input("Masukkan Nilai : "))
if(nilai>=85):
    mutu = "A"
elif(nilai>=75):
    mutu = "B"
elif(nilai>=55):
    mutu = "C"
elif(nilai>=40):
    mutu = "D"
else:
    mutu = "E"
print("Nilai Anda: ", nilai)
print("Nilai Anda: ", mutu)