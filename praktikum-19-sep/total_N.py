N = int(input("Masukkan jumlah data (N): "))

total = 0

for i in range(1, N+1):
    data = int(input(f"Masukkan data ke-{i}: "))
    total += data

rata_rata = total / N


print(f"Total penjumlahan: {total}")
print(f"Rata-rata: {rata_rata}")
 