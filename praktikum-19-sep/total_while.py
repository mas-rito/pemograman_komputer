total = 0
i = 0
c = 0

while True:
    c = int(input("Masukkan bilangan: "))

    if c == -100:
        break

    else:
        total = total + c
        i = i + 1
        print("Total setiap perulangan: ", total)

print("Total: ", total)
print("Rata-rata: ", total / i)