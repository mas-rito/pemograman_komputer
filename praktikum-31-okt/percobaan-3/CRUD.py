def read():
    with open('data.txt', 'r') as file:
        content = file.read()
        return content

def create():
    with open('data.txt', 'a') as file:
        item = input("Masukkan item yang ingin ditambahkan: ")
        file.write(item + "\n")
        print(f"\nItem '{item}' berhasil ditambahkan.")

def update():
    data = read().splitlines()
    index = int(input("Masukkan indeks item yang ingin diperbarui: "))
    new_item = input("Masukkan item baru: ")
    if index >= 0 and index < len(data):
        data[index] = new_item
        with open('data.txt', 'w') as file:
            file.write('\n'.join(data))
        print(f"\nItem pada indeks {index} berhasil diperbarui.")
    else:
        print(f"\nIndeks {index} tidak valid.")

def delete():
    data = read().splitlines()
    index = int(input("Masukkan indeks item yang ingin dihapus: "))
    if index >= 0 and index < len(data):
        del data[index]
        with open('data.txt', 'w') as file:
            file.write('\n'.join(data))
        print(f"\nItem pada indeks {index} berhasil dihapus.")
    else:
        print(f"\nIndeks {index} tidak valid.")
