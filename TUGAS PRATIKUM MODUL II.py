print("\n~ Selamat Datang di LAF11 Caffe ~\nmakan di sini di jamin kenyang, silahkan dipilih")

print("\nDaftar Paket Makanan:")
print("----------------------------------------------------------")
print("|Paket |            Termasuk                 | Harga     |")
print("----------------------------------------------------------")
print("|  1   | Nasi Goreng + Es Teh                | Rp30.000  |")
print("|  2   | Mie Goreng + Es Jeruk               | Rp25.000  |")
print("|  3   | Ayam Bakar + Nasi Putih + Es Jeru   | Rp30.000  |")
print("|  4   | Sate Ayam + Nasi Putih + Es Teh     | Rp30.000  |")
print("|  5   | Ikan Bakar + Nasi Putih + Es Jeruk  | Rp45.000  |")
print("|  5   | Sop Iga Sapi + Nasi Putih + Es Jeruk| Rp60.000  |")
print("----------------------------------------------------------")

print("\nSilakan masukkan data diri Anda")
nama = input("Nama                     : ")
no_telepon = input("Nomor Telepon            : ")
alamat = input("Alamat Pengiriman        : ")

paket = input("Masukkan kode paket (1-6): ")
if paket == "1":
    harga = 30000
    isi = "Nasi Goreng + Es Teh"
elif paket == "2":
    harga = 25000
    isi = "Mie Goreng + Es Jeruk"
elif paket == "3":
    harga = 30000
    isi = "Ayam Bakar + Nasi Putih + Es Jeruk"
elif paket == "4":
    harga = 30000
    isi = "Sate Ayam + Nasi Putih + Es Teh"
elif paket == "5":
    harga = 45000
    isi = "Ikan Bakar + Nasi Putih + Es Jeruk"
elif paket == "6":
    harga = 60000
    isi = "Sop Iga Sapi + Nasi Putih + Es Jeruk"
else:
    print("Kode paket tidak valid!")
    harga = 0
    isi = "Paket tersebut belum tersedia"

jumlah = int(input("Masukkan jumlah paket    : "))
total_harga = harga * jumlah

pajak = total_harga * 0.1
if total_harga == 0:
    biaya_pengiriman = 0
elif total_harga < 150000:
    biaya_pengiriman = 25000
else:
    biaya_pengiriman = 0
total_akhir = total_harga + pajak + biaya_pengiriman

print("\n================ STRUK PEMESANAN ===============")
print("Nama             : " + nama)
print("Nomor Telepon    : " + no_telepon)
print("Alamat Pengiriman: " + alamat)
print("\nDetail Pesanan   :")
print("-Paket ", paket,"\n(", isi, ")",int(jumlah),"x","Rp.",(harga ))
print("\nTotal Harga      : Rp" + str(total_harga))
print("Pajak (10%)      : Rp" + str(pajak))
print("Biaya Pengiriman : Rp" + str(biaya_pengiriman))
print("------------------------------------------------")
print("Total Akhir      : Rp" + str(total_akhir))
print("================================================")
print("Terima kasih, selamat menikmati")