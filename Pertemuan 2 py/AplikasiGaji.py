# Input data
nip = input("Masukkan NIP: ")
nama = input("Masukkan Nama: ")
jk = input("Masukkan JK (jenis kelamin L / P): ")
masa_kerja = int(input("Masukkan masa kerja: "))
status_pernikahan = input("Masukkan status pernikahan (Single(S)/Janda (J)/Duda(D)/Menikah (M)): ")
jumlah_anak = int(input("Masukkan jumlah anak: "))

# Hitung gaji pokok
if masa_kerja <= 2:
  gaji_pokok = 2000000
elif masa_kerja <= 5:
  gaji_pokok = 3000000
elif masa_kerja <= 10:
  gaji_pokok = 5000000
else:
  gaji_pokok = 7500000

# Hitung tunjangan istri
tunjangan_istri = 0
if jk == "L" and status_pernikahan == "M":
  tunjangan_istri = 0.1 * gaji_pokok

# Hitung tunjangan anak
tunjangan_anak = 0
if jk == "L" and status_pernikahan == "M":
  tunjangan_anak = 0.05 * gaji_pokok * jumlah_anak

# Hitung total penghasilan
total_penghasilan = gaji_pokok + tunjangan_istri + tunjangan_anak

# Output
print("==========================================")
print("NIP:", nip)
print("Nama:", nama)
print("JK:", jk)
print("Gaji pokok:", gaji_pokok)
print("Tunjangan Istri:", tunjangan_istri)
print("Tunjangan Anak:", tunjangan_anak)
print("Total Penghasilan:", total_penghasilan)