def baca_data_mahasiswa(nama_file):
    with open(nama_file, 'r') as file:
        return file.read()

def input_data_mahasiswa():
    nama = input("Masukan nama mahasiswa: ")
    nim = input('Masukan nim mahasiswa: ')
    prodi = input('Masukan prodi mahasiswa: ')

    with open('data.txt', 'a') as file:
        file.write(f'Nama = {nama}\nNIM = {nim}\nProdi = {prodi}\n\n')

    print(baca_data_mahasiswa('data.txt'))

print("Input data mahasiswa")
print("--------------------")
input_data_mahasiswa()