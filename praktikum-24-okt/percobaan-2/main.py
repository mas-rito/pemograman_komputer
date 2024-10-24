# Buatlah program kalkulator sederhana dimana operasi aritmatikanya menggunakan
# yang dibuat sendiri.Dan panggil menggunakan program utamanya pada file kode
# yang berbeda.

import aritmatika


print("Selamat datang di kalkulator sederhana")
print('======================================')
print('Masukan perhitunganmu, cth: 2 + 2')
perhitungan = input()

angka1, operator, angka2 = aritmatika.memecah_input(perhitungan)

if operator == '+':
    print(f"{angka1} + {angka2} = {aritmatika.penambahan(angka1, angka2)}")
elif operator == '-':
    print(f"{angka1} - {angka2} = {aritmatika.pengurangan(angka1, angka2)}")
elif operator == 'x':
    print(f"{angka1} x {angka2} = {aritmatika.perkalian(angka1, angka2)}")
elif operator == '/':
    print(f"{angka1} / {angka2} = {aritmatika.pembagian(angka1, angka2)}")
else:
    print("Operasi tidak valid")