# jumlah_lulus = 0
# jumlah_tidak_lulus = 0

# while True:
#     print("Masukkan kategori nilai mahasiswa (A, B, C, D, E) atau 'selesai' untuk melihat hasil: ")
#     kategori_nilai = input(f"Masukkan kategori nilai mahasiswa: ")

#     if kategori_nilai == "A" or kategori_nilai == "B" or kategori_nilai == "C":
#         jumlah_lulus += 1
#     elif kategori_nilai == "D" or kategori_nilai == "E":
#         jumlah_tidak_lulus += 1
#     elif kategori_nilai == "selesai":
#         break

# print(f'Jumlah mahasiswa yang lulus: {jumlah_lulus} dan yang tidak lulus: {jumlah_tidak_lulus} dari {jumlah_lulus + jumlah_tidak_lulus} mahasiswa')


jumlah_lulus = 0
jumlah_tidak_lulus = 0
list_nilai = []

i =1
while True:
    print("Masukkan nilai mahasiswa atau 999 untuk melihat hasil: ")
    nilai = int(input(f"Masukkan nilai mahasiswa: "))

    if nilai == 999:
        break

    if nilai >= 85:
        data = {"Mahasiswa":i,"Nilai": nilai, "Kategori": "A"}
        list_nilai.append(data)
        jumlah_lulus += 1
    elif nilai >= 70:
        data = {"Mahasiswa":i,"Nilai": nilai, "Kategori": "B"}
        list_nilai.append(data)
        jumlah_lulus += 1
    elif nilai >= 60:
        data = {"Mahasiswa":i,"Nilai": nilai, "Kategori": "C"}
        list_nilai.append(data)
        jumlah_lulus += 1
    elif nilai < 60:
        data = {"Mahasiswa":i,"Nilai": nilai, "Kategori": "D"}
        list_nilai.append(data)
        jumlah_tidak_lulus += 1
    else:
        data = {"Mahasiswa":i,"Nilai": nilai, "Kategori": "E"}
        list_nilai.append(data)
        jumlah_tidak_lulus += 1
    i += 1
    

print('------------------')
print('HASIL PERHITUNGAN')
print('------------------')

for data in list_nilai:
    for key, value in data.items():
        print(f'{key}: {value}')
    print()

print(f'Jumlah mahasiswa yang lulus: {jumlah_lulus} dan yang tidak lulus: {jumlah_tidak_lulus} dari {jumlah_lulus + jumlah_tidak_lulus} mahasiswa')