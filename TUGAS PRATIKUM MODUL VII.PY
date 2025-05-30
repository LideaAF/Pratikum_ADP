def input_data_praktikan():
    praktikan = []
    while True:
        nama = input("Masukkan nama praktikan (atau ketik 'selesai' untuk mengakhiri): ")
        if nama.lower() == 'selesai':
            break
        nim = input("Masukkan NIM praktikan: ")
        pretest = float(input("Masukkan nilai pretest: "))
        posttest = float(input("Masukkan nilai posttest: "))
        tugas = float(input("Masukkan nilai tugas/makalah: "))
        bonus = float(input("Masukkan nilai bonus: "))
        praktikan.append({'nama': nama, 'nim': nim, 'pretest': pretest, 'posttest': posttest, 'tugas': tugas, 'bonus': bonus})
    return praktikan

def hitung_nilai_akhir(praktikan):
    for p in praktikan:
        p['nilai_akhir'] = (0.25 * p['pretest'] + 0.25 * p['posttest'] + 0.50 * p['tugas']) + p['bonus']

def urutkan_praktikan(praktikan):
    n = len(praktikan)
    for i in range(n):
        for j in range(0, n - i - 1):
            if praktikan[j]['nilai_akhir'] < praktikan[j + 1]['nilai_akhir']:
                praktikan[j], praktikan[j + 1] = praktikan[j + 1], praktikan[j]
    return praktikan

def tampilkan_hasil(praktikan):
    print ("DATA PRATIKAN SHIF V")
    print("\n{:<15} {:<12} {:<12} {:<10}".format("Nama", "NIM", "Nilai Akhir", "Peringkat"))
    print("=" * 52)
    total_nilai_akhir = 0
    peringkat = 1
    for p in praktikan:
        print("{:<15} {:<12} {:<12.2f} {:<10}".format(p['nama'], p['nim'], p['nilai_akhir'], peringkat))
        total_nilai_akhir += p['nilai_akhir']
        peringkat += 1
    rata_nilai_akhir = total_nilai_akhir / len(praktikan) if praktikan else 0
    print("=" * 52)
    print("{:<27} {:<12.2f}".format("Rata-rata Nilai Akhir  ", rata_nilai_akhir))

def main():
    praktikan = input_data_praktikan()
    if not praktikan:
        print("Tidak ada data praktikan yang dimasukkan.")
        return  
    hitung_nilai_akhir(praktikan)
    praktikan_terurut = urutkan_praktikan(praktikan)
    tampilkan_hasil(praktikan_terurut)

if __name__ == "__main__":
    main()
