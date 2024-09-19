while True:
    data = int(input("Masukkan data bilangan: "))

    if data > 0:
        print("Anda memasukan nilai positif pada program ini")
    elif data < 0:
        print("Input tidak boleh negatif")
        break
    else:
        print("Bilangan nol")
        break