def hitung_biaya_warnet(jam_masuk, menit_masuk, detik_masuk, jam_keluar, menit_keluar, detik_keluar, tarif_per_jam):
  def konversi_ke_detik(jam, menit, detik):
    return jam * 3600 + menit * 60 + detik

  total_detik_masuk = konversi_ke_detik(jam_masuk, menit_masuk, detik_masuk)
  total_detik_keluar = konversi_ke_detik(jam_keluar, menit_keluar, detik_keluar)

  selisih_detik = total_detik_keluar - total_detik_masuk

  jam_pakai = selisih_detik // 3600
  sisa_detik = selisih_detik % 3600
  menit_pakai = sisa_detik // 60
  detik_pakai = sisa_detik % 60

  biaya = jam_pakai * tarif_per_jam

  return (jam_pakai, menit_pakai, detik_pakai), biaya

print("----------------")
jam_masuk = int(input("Masukkan jam mulai: "))
menit_masuk = int(input("Masukkan menit mulai: "))
detik_masuk = int(input("Masukkan detik mulai: "))
print("----------------")
jam_keluar = int(input("Masukkan jam selesai: "))
menit_keluar = int(input("Masukkan menit selesai: "))
detik_keluar = int(input("Masukkan detik selesai: "))
tarif = 5000

lama_pakai, biaya = hitung_biaya_warnet(jam_masuk, menit_masuk, detik_masuk, jam_keluar, menit_keluar, detik_keluar, tarif)

print("----------------")
print("Lama pemakaian:", lama_pakai[0], "jam", lama_pakai[1], "menit", lama_pakai[2], "detik")
print("Total biaya: Rp", biaya)