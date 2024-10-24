# Buatlah modul untuk memanipulasi data pada sebuah list dengan fungsi dasar
# CRUD (create, read, update, delete). Buat program utamanya pada file kode yang
# berbeda.

def read(data):
    return data

def create(data, item):
    data.append(item)
    return data

def update(data, index, new_item):
    if index >= 0 and index < len(data):
        data[index] = new_item
        return True
    else:
        return False

def delete(data, index):
    if index >= 0 and index < len(data):
        del data[index]
        return True
    else:
        return False

def main():
    data = []
    
    while True:
        print("\nData saat ini:", read(data))
        print("\nMenu:")
        print("1. Tambah item (Create)")
        print("2. Lihat data (Read)")
        print("3. Perbarui item (Update)")
        print("4. Hapus item (Delete)")
        print("5. Keluar")

        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == "1":
            item = input("Masukkan item yang ingin ditambahkan: ")
            create(data, item)
            print(f"Item '{item}' berhasil ditambahkan.")
        
        elif pilihan == "2":
            print("\nData saat ini:", read(data))
        
        elif pilihan == "3":
            index = int(input("Masukkan indeks item yang ingin diperbarui: "))
            new_item = input("Masukkan item baru: ")
            if update(data, index, new_item):
                print(f"Item pada indeks {index} berhasil diperbarui.")
            else:
                print(f"Indeks {index} tidak valid.")
        
        elif pilihan == "4":
            index = int(input("Masukkan indeks item yang ingin dihapus: "))
            if delete(data, index):
                print(f"Item pada indeks {index} berhasil dihapus.")
            else:
                print(f"Indeks {index} tidak valid.")
        
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Coba lagi.")


main()