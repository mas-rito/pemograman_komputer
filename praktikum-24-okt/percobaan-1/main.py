# Buatlah modul untuk memanipulasi data pada sebuah list dengan fungsi dasar
# CRUD (create, read, update, delete). Buat program utamanya pada file kode yang
# berbeda.

import CRUD

def main():
    data = []
    
    while True:
        # print("\nData saat ini:", CRUD.read(data))
        print("\nMenu:")
        print("1. Tambah item (Create)")
        print("2. Lihat data (Read)")
        print("3. Perbarui item (Update)")
        print("4. Hapus item (Delete)")
        print("5. Keluar")

        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == "1":
            CRUD.create(data)
        
        elif pilihan == "2":
            CRUD.read(data)
        
        elif pilihan == "3":
            CRUD.update(data)
        
        elif pilihan == "4":
            CRUD.delete(data)
        
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Coba lagi.")


main()