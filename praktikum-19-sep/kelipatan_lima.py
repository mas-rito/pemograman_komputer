
nilai = int(input("Masukkan bilangan integer: "))
jumlah = 0

for i in range(1, nilai+1):
    if i % 5 == 0:
        jumlah += i
        print('Bilangan kelipatan 5:', i)
    

print("Total jumlah kelipatan 5 dari 1 sampai", nilai, "adalah", jumlah)
