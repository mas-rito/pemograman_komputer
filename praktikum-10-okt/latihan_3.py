list_nama = []
list_nilai_tugas = []
list_nilai_UTS = []
list_nilai_UAS = []

while True:
    nama = input("Masukan nama mahasiswa: ")
    nilai_tugas = int(input("Masukan nilai tugas: "))
    nilai_uts = int(input("Masukan Nilai UTS: "))
    nilai_uas = int(input("Masukan Nilai UAS: "))

    list_nama.append(nama)
    list_nilai_tugas.append(nilai_tugas)
    list_nilai_UTS.append(nilai_uts)
    list_nilai_UAS.append(nilai_uas)

    ulang = input("Apakah ada data lagi? (y/t): ")
    if ulang == "t":
        break

for i in range(len(list_nama)):
    nilai_murni_tugas = list_nilai_tugas[i] * 30/100
    nilai_murni_UTS = list_nilai_UTS[i] * 30/100
    nilai_murni_UAS = list_nilai_UAS[i] * 40/100

    print(f"Nama: {list_nama[i]}")
    print(f"Nilai Tugas: {nilai_murni_tugas}")
    print(f"Nilai UTS: {nilai_murni_UTS}")
    print(f"Nilai UAS: {nilai_murni_UAS}")
    print(f"Nilai Akhir: {nilai_murni_tugas + nilai_murni_UTS + nilai_murni_UAS}")
    print("----------------")

for i in range(len(list_nama)):
    nilai_murni_tugas = list_nilai_tugas[i] * 30/100
    nilai_murni_UTS = list_nilai_UTS[i] * 30/100
    nilai_murni_UAS = list_nilai_UAS[i] * 40/100
    nilai_akhir = nilai_murni_tugas + nilai_murni_UTS + nilai_murni_UAS

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

    print(f"Nama: {list_nama[i]}")
    print(f"Grade nilai akhir : {grade}")