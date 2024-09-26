# Buatlah table perkalian dari angka yang dimasukkan


# for i in range(1,11):
#     print(f'{i} x {bilangan} = {i * bilangan}')

# for i in range(10):
#     print(f'{i+1} x {bilangan} = {(i + 1) * bilangan}')


bilangan = int(input("Masukkan bilangan: "))

i = 1
while i <= 10:
    print(f'{i} x {bilangan} = {i * bilangan}')
    i = i + 1
    # if i > 10:
    #     break
