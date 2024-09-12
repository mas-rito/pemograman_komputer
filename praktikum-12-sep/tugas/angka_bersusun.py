bilangan_1 = int(input("Masukkan bilangan ke-1: "))
bilangan_2 = int(input("Masukkan bilangan ke-2: "))
bilangan_3 = int(input("Masukkan bilangan ke-3: "))

array = [bilangan_1, bilangan_2, bilangan_3]

array.sort(reverse=True)

print(array)