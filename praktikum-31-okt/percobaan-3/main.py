import CRUD

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah item (Create)")
        print("2. Lihat data (Read)")
        print("3. Perbarui item (Update)")
        print("4. Hapus item (Delete)")
        print("5. Keluar")

        
        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == "1":
            CRUD.create()
        
        elif pilihan == "2":
            data=CRUD.read()
            print(data)
        
        elif pilihan == "3":
            CRUD.update()
        
        elif pilihan == "4":
            CRUD.delete()
        
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Coba lagi.")


main()