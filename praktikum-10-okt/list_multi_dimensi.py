list_makanan = [
    ['Siomay', 'Bakso', 'Nasi Goreng'],
    ['Soto', 'Nasi Goreng', 'Ayam Geprek'],
    ['Sate', 'Tahu', 'Tempe']
]

print(list_makanan[1][0])

for i in list_makanan:
    print(' ')
    for j in i:
        print(j, end=' ')
    
print(' ')