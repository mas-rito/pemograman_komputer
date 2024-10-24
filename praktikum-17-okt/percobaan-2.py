import random

def generate_random_number(bawah, atas):
    return random.randint(bawah, atas)

def guess_number(number):
    jumlah_tebakan = 0
    while True:
        print('=======================')
        guess = int(input("Masukan angka tebakan mu: "))

        if guess == number:
            print("Selamat, kamu benar!")
            print(f"Jumlah tebakanmu: {jumlah_tebakan}")
            break
        elif guess < number:
            print("Terlalu kecil, coba lagi")
        else:
            print("Terlalu besar, coba lagi")

        jumlah_tebakan += 1
        

batas_atas = int(input("Masukan angka batas atas: "))
batas_bawah = int(input("Masukan angka batas bawah: "))

angka_tebakan = generate_random_number(batas_bawah, batas_atas)

guess_number(angka_tebakan)