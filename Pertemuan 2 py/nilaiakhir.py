print("=======================================")
print("Aplikasi untuk menghitung nilai mahasiswa")
print("Nama : Hamdan Sadad")
print("Kelas : TI23B ")
print("=======================================")

kehadiran = int(input("Masukkan nilai kehadiran: "))
uas = int(input("Masukkan nilai uts: "))
uts = int(input("Masukkan nilai uas: "))
tugas = int(input("Masukkan nilai tugas: "))

nilai_kehadiran = kehadiran * 0.30
nilai_uts = uts * 0.20
nilai_uas = uas * 0.20
nilai_tugas = tugas * 0.30
nilai_akhir = nilai_kehadiran + nilai_uts + nilai_uas + nilai_tugas

if(nilai_akhir>=85):
    mutu = "A"
elif(nilai_akhir>=75):
    mutu = "B"
elif(nilai_akhir>=55):
    mutu = "C"
elif(nilai_akhir>=40):
    mutu = "D"
else:
    mutu = "E"
print("Nilai Anda: ", nilai_akhir)
print("Nilai Anda: ", mutu)