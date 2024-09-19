def select_input():
    options = ["Penambahan", "Pengurangan", "Perkalian", "Pembagian"]

    print("Pilih operasi aritmatika:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    while True:
        try:
            selected_index = int(input("Masukan nomor pilihanmu: ")) - 1
            if selected_index < 0 or selected_index >= len(options):
                print("Pilihanmu tidak valid. Silakan coba lagi.")
            else:
                selected_value = options[selected_index]
                print("Pilihanmu:", selected_value)
                break
        except ValueError:
            print("Pilihanmu tidak valid. Silakan coba lagi.")

    return selected_value

selected_value = select_input()
number1 = int(input("Masukkan angka pertama: "))
number2 = int(input("Masukkan angka kedua: "))

if selected_value == "Penambahan":
    result = number1 + number2
elif selected_value == "Pengurangan":
    result = number1 - number2
elif selected_value == "Perkalian":
    result = number1 * number2
elif selected_value == "Pembagian":
    result = number1 / number2

print("Hasilnya:", result)