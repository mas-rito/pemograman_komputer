bil = int(input("Masukkan bilangan: "))

faktorial = 1

if bil < 0:
    print("Faktorial tidak terdefinisi untuk bilangan negatif.")
elif bil == 0:
    faktorial = 1
else:
    for i in range(1, bil + 1):
        faktorial *= i

    print(f"Faktorial dari {bil} adalah {faktorial}")
