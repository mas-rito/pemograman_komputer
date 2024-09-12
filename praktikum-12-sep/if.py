angka = 7

mod= angka % 2

if mod == 0:
    print("Genap")
else:
    print("Ganjil")

#informatif
input = int(input("Masukkan angka: "))

if input % 2 == 0:
    print(f'Angka {input} adalah bilangan genap')
else:
    print(f'Angka {input} adalah bilangan ganjil')

#if else
nilai = 78

if nilai >= 80:
    print("Nilai A")
elif nilai >= 70:
    print("Nilai B")
elif nilai >= 60:
    print("Nilai C")
else:
    print("Nilai D")

#Nested if
umur =25
mandiri = True

if umur >= 22:
    if mandiri == True:
        print("Temui orang tuanya")
    else:
        print("Semangat semangat semangata!")
else:
    print("Anda belum boleh menikah")