total = 0

while True:
    bilangan = int(input("Masukkan bilangan (0 untuk berhenti): "))

    if bilangan == 0:
        break

    total += bilangan

print("Total:", total)