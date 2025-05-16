
nomor_mahasiswa = []
nama_mahasiswa = []
nilai_mahasiswa = []

nomor_berikutnya = 1

while True:
    print("\nMenu Manajemen Nilai Mahasiswa")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")
    pilihan = input("Pilih menu salah satu di atas (1-4): ")

    if pilihan == '1':
        print("\nTambah Data Mahasiswa")
        nama = input("Masukkan nama mahasiswa: ")
        while True:
            try:
                nilai = float(input("Masukkan nilai mahasiswa (0-100): "))
                if 0 <= nilai <= 100:
                    break
                else:
                    print("Nilai harus antara 0 dan 100. Coba lagi.")
            except ValueError:
                print("Masukkan angka yang valid untuk nilai.")
        nomor_mahasiswa.append(nomor_berikutnya)
        nama_mahasiswa.append(nama)
        nilai_mahasiswa.append(nilai)
        nomor_berikutnya += 1
        print(f"Data mahasiswa '{nama}' berhasil ditambahkan dengan nomor {nomor_berikutnya - 1}.")

    elif pilihan == '2':
        print("\nHapus Data Mahasiswa")
        if len(nomor_mahasiswa) == 0:
            print("Data mahasiswa masih kosong")
        else:
            try:
                nomor_hapus = int(input("Masukkan nomor mahasiswa yang akan dihapus: "))
                if nomor_hapus in nomor_mahasiswa:
                    index = nomor_mahasiswa.index(nomor_hapus)
                    nama_hapus = nama_mahasiswa[index]
                    del nomor_mahasiswa[index]
                    del nama_mahasiswa[index]
                    del nilai_mahasiswa[index]
                    print(f"Data mahasiswa dengan nomor {nomor_hapus} ('{nama_hapus}') berhasil dihapus.")
                else:
                    print(f"Tidak ditemukan data mahasiswa dengan nomor {nomor_hapus}.")
            except ValueError:
                print("Input nomor mahasiswa tidak valid.")

    elif pilihan == '3':
        print("\nData Mahasiswa dari nilai tertinggi ke terendah")
        if len(nomor_mahasiswa) == 0:
            print("Belum ada data mahasiswa.")
        else:
            nilai_index = list(enumerate(nilai_mahasiswa))
            nilai_index.sort(key=lambda x: x[1], reverse=True)
            print("{:<6} {:<20} {:<10}".format("Nomor", "Nama", "Nilai"))
            print("-" * 38)
            for idx, _ in nilai_index:
                print("{:<6} {:<20} {:<10}".format(nomor_mahasiswa[idx], nama_mahasiswa[idx], nilai_mahasiswa[idx]))
  
    elif pilihan == '4':
        print("Keluar dari program. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")