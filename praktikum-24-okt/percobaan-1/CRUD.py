def read(data):
    print("\nData saat ini:", data)

def create(data):
    item = input("Masukkan item yang ingin ditambahkan: ")
    data.append(item)
    print(f"\nItem '{item}' berhasil ditambahkan.")

def update(data):
    index = int(input("Masukkan indeks item yang ingin diperbarui: "))
    new_item = input("Masukkan item baru: ")
    if index >= 0 and index < len(data):
        data[index] = new_item
        print(f"\nItem pada indeks {index} berhasil dihapus.")
    else:
        print(f"\nIndeks {index} tidak valid.")

def delete(data):
    index = int(input("Masukkan indeks item yang ingin dihapus: "))
    if index >= 0 and index < len(data):
        del data[index]
        print(f"\nItem pada indeks {index} berhasil dihapus.")
    else:
        print(f"\nIndeks {index} tidak valid.")
