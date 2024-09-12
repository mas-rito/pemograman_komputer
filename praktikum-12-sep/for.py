# perulangan for range
jumlahdata =10

for i in range(jumlahdata):
    print('cetak perulangan ke -', i + 1)

print('------------------')

# perulangan for in array
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for angka in array:
    print(angka)

print('------------------')
# perulangan for range (start, stop, step)

for i in range(5, 2, -1):
    print('data ke -',i)

print('------------------')

for i in range(5,8):
    print('data ke -',i)

print('------------------')
# perulangan for with break and continue
print('perulangan with break')
for i in range(10, 20):
    if i == 15:
        break
    print('data ke -', i)

print('perulangan with continue')
for i in range(10, 20):
    if i == 15:
        continue
    print('data ke -', i)