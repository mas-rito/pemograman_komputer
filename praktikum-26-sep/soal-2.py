# total_suhu = 0
# suhu_tertinggi = 0
# suhu_terendah = 99999999
# for i in range(5):
#     suhu = int(input("Masukkan suhu: "))
#     total_suhu += suhu

#     if suhu > suhu_tertinggi:
#         suhu_tertinggi = suhu

#     if suhu < suhu_terendah:
#         suhu_terendah = suhu

# rata_rata = total_suhu / 5
# print("Rata-rata suhu: ", rata_rata)
# print("Suhu tertinggi: ", suhu_tertinggi)
# print("Suhu terendah: ", suhu_terendah)

list_suhu = []

for i in range(5):
    suhu = int(input("Masukkan suhu: "))
    list_suhu.append(suhu)

rata_rata = sum(list_suhu) / len(list_suhu)
print("Rata-rata suhu: ", rata_rata)
print("Suhu tertinggi: ", max(list_suhu))
print("Suhu terendah: ", min(list_suhu))