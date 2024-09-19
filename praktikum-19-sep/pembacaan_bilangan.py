
bilangan_ganjil = 0
bilangan_genap = 0

print("Masukkan bilangan negatif untuk berhenti.")
while True:
    bil = int(input("Masukkan bilangan: "))

    if bil < 0:
        break

    if bil % 2 == 0:
        bilangan_genap += 1
    else:
        bilangan_ganjil += 1

print("Jumlah bilangan genap:", bilangan_genap)
print("Jumlah bilangan ganjil:", bilangan_ganjil)