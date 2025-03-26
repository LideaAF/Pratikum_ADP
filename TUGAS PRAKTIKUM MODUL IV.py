print("Selamat datang di Form Penilaian Calon Tim Pengajar")
print("Himpunan Mahasiswa dan Sains Data")
print("-" * 35)

jumlah_pendaftar = int(input("Input Jumlah Pendaftar: "))
print("-" * 35)

for i in range(jumlah_pendaftar):
    print(f"\nData Pendaftar ke-{i+1}")
    print("-" * 20)
    nama = input("Nama: ")
    mata_kuliah = input("Mata kuliah yang diminati: ")

    while True :
        try:
            nilai_wawancara = int(input("Nilai wawancara (1-100): "))
            if  1<=nilai_wawancara<=100:
                break
            else:
                print("Penilaian harus berada dalam rentang 1-100.")
        except ValueError:
                print("Penilaian harus berupa angka dan dalam rentang 1-100.")        

    while True :
        try:
            nilai_tes_tulis = int(input("Nilai tes tulis (1-100): "))
            if  1<=nilai_tes_tulis<=100:
                break
            else:
                print("Penilaian harus berada dalam rentang 1-100.") 
        except ValueError:
                print("Penilaian harus berupa angka dan dalam rentang 1-100.")

    while True :
        try:
            nilai_mengajar = int(input("Nilai mengajar (1-100): "))
            if  1<=nilai_mengajar<=100:
                break
            else:
                print("Penilaian harus berada dalam rentang 1-100.")
        except ValueError:
                print("Penilaian harus berupa angka dan dalam rentang 1-100.")
                
    nilai_rata_rata = (nilai_wawancara + nilai_tes_tulis + nilai_mengajar) / 3
    if nilai_rata_rata > 80:
        predikat = "LULUS"
    else:
        predikat = "TIDAK LULUS"
    print(f"Predikat: {predikat}")
    print("-" * 20)

print("\nTerima kasih telah menggunakan Form Penilaian.")
print ("-" * 35)