print("=== Program Menghitung Jarak Antar Titik ===")
while True:
    try:
        n = int(input("Masukkan jumlah titik (n): "))
        if n <= 0:
            print("Input harus bilangan bulat positif, coba lagi.")
            continue
        break
    except:
        print("Input tidak valid, masukkan bilangan bulat.")

titik = []
i = 0
while i < n:
    koordinat = input("Masukkan koordinat titik ke-{} (x,y),: ".format(i+1))
    try:
        x_str, y_str = koordinat.split(",")
        x, y = int(x_str), int(y_str) 
        titik.append([x,y])
        i += 1
    except:
        print("Input tidak valid, pastikan format x,y dan angka valid.")

print("\nTitik yang dimasukkan:")
i = 0
while i < n:
    t = titik[i]
    print("Titik {}: ({}, {})".format(i+1, t[0], t[1]))
    i += 1

print("\nJarak antar titik:")
i = 0
while i < n:
    j = i + 1
    while j < n:
        dx = titik[i][0] - titik[j][0]
        dy = titik[i][1] - titik[j][1]
        jarak = (dx*dx + dy*dy)**0.5 
        print("Jarak titik {} dan titik {} = {:.3f}".format(i+1, j+1, jarak))
        j += 1
    i += 1
print("===    Program selesai & Terima kasih     ===")
