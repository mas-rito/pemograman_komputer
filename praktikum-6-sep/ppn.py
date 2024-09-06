print("Menghitung PPN")
harga_barang = int(input("Masukkan harga barang: Rp "))

ppn = harga_barang * 12.5/100
total_harga = harga_barang + ppn

print("----------------")
print("Detail Barang")
print("----------------")
print("Harga barang: Rp ", int(harga_barang))
print("PPN 12.50%: Rp ", int(ppn))
print("Total harga: Rp ", int(total_harga))