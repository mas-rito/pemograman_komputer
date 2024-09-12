nim = input("Masukkan NIM: ")
nama = input("Masukkan Nama: ")
matakuliah = input("Masukkan Matakuliah: ")
kehadiran = int(input("Masukkan Kehadiran: "))
tugas = int(input("Masukkan Nilai Tugas: "))
uts = int(input("Masukkan Nilai UTS: "))
uas = int(input("Masukkan Nilai UAS: "))

nilai_akhir = (kehadiran * 0.1) + (tugas * 0.2) + (uts * 0.3) + (uas * 0.4)
grade = "E"

if nilai_akhir >= 80:
    grade = "A"
elif nilai_akhir >= 70:
    grade = "B"
elif nilai_akhir >= 60:
    grade = "C"
elif nilai_akhir >= 50:
    grade = "D"
else:
    grade = "E"

print("----------------")
print("Data Mahasiswa")
print("----------------")
print(f"NIM: {nim}")
print(f"Nama: {nama}")
print(f"Mata Kuliah: {matakuliah}")
print(f"Kehadiran: {kehadiran}")
print(f"Nilai Tugas: {tugas}")
print(f"Nilai UTS: {uts}")
print(f"Nilai UAS: {uas}")
print(f"Nilai Akhir: {grade}")
