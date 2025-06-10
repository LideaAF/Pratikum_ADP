def load_data(file='data_keuangan.txt'):
    try:
        with open(file) as f:
            return [line.strip().split('|') for line in f if line.strip()]
    except:
         return []

def save_data(data, file='data_keuangan.txt'):
    with open(file, 'w') as f:
        f.writelines('|'.join(d)+'\n' for d in data)

def tambah(data):
    tgl = input('Tanggal (YYYY-MM-DD): ').strip()
    ket = input('Keterangan: ').strip()
    while True:
        jum = input('Jumlah: ').strip()
        if jum.isdigit(): 
            break
        print('Jumlah harus angka.')
    while True:
        tipe = input('Tipe (pengeluaran/pemasukan): ').strip().lower()
        if tipe in ('pengeluaran','pemasukan'):
            break
        print('Tipe harus pengeluaran atau pemasukan.')
    data.append([tgl,ket,jum,tipe])
    print('Data ditambahkan.\n')

def hapus(data):
    if not data:
        print('Tidak ada data.\n')
        return
    for i,d in enumerate(data,1):
        print(f"{i}. {d[0]} | {d[1]} | {d[2]} | {d[3]}")
    while True:
        x = input('Hapus nomor (0 batal): ').strip()
        if x.isdigit():
            x=int(x)
            if x==0:
                print('Batal.\n')
                return
            if 1 <= x <= len(data):
                data.pop(x-1)
                print('Data dihapus.\n')
                return
        print('Nomor tidak valid.')

def tampil(data):
    if not data:
        print('Belum ada data.\n')
        return
    print(f"\n{'No':<3} {'Tanggal':<12} {'Keterangan':<25} {'Jumlah':>10} {'Tipe':<12}")
    print('-'*66)
    for i,d in enumerate(data,1):
        print(f"{i:<3} {d[0]:<12} {d[1]:<25} {d[2]:>10} {d[3]:<12}")
    print()

def main():
    data=load_data()
    while True:
        print('Menu: 1.Tambah 2.Hapus 3.Tampil 4.Keluar')
        p=input('Pilih: ').strip()
        if p=='1':
            tambah(data); save_data(data)
        elif p=='2':
            hapus(data); save_data(data)
        elif p=='3':
            tampil(data)
        elif p=='4':
            print('Terima kasih!'); break
        else:
            print('Pilihan salah.\n')

if __name__=='__main__':
    main()

