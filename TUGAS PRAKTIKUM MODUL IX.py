import pygame
import sys
import math

pygame.init()
lebar_layar, tinggi_layar = 800, 400
FPS = 50
lebar_tiang = 20
tinggi_tiang = 350
lebar_bendera = 200
tinggi_bendera = 110
amplitudo_gel = 10
frekuaensi_gel = 0.02
jumlah_poin = 50

merah = (227, 27, 35)
putih = (255, 255, 255)
coklat = (150, 69, 19)
langit = (235, 235, 255)

layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption("Bendera merah putih berkibar di langit yang cerah")

def gambar_bendera(x, y, offset):
    poin_atas = []
    poin_bawah = []

    for i in range(jumlah_poin + 1):
        frac = i / jumlah_poin
        xi = x + frac * lebar_bendera
        yi_offset = amplitudo_gel * math.sin(frekuaensi_gel * (frac * 300 + offset))
        poin_atas.append((xi, y + yi_offset))
        poin_bawah.append((xi, y + tinggi_bendera + yi_offset))
    poin_tengah = [(px, py + tinggi_bendera // 2) for (px, py) in poin_atas]
    pygame.draw.polygon(layar, merah, poin_atas + poin_tengah[::-1])
    pygame.draw.polygon(layar, putih, poin_tengah + poin_bawah[::-1])

def utama():
    jam = pygame.time.Clock()
    offset = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        layar.fill(langit)
        tiang_x = lebar_layar // 4
        tiang_y = tinggi_layar - tinggi_tiang
        pygame.draw.rect(layar, coklat, (tiang_x, tiang_y, lebar_tiang, tinggi_tiang), border_radius=4)
        offset += 2
        if offset > 10000:
            offset = 0
        bendera_x = tiang_x + lebar_tiang
        bendera_y = tiang_y
        gambar_bendera(bendera_x, bendera_y, offset)

        pygame.display.flip()
        jam.tick(FPS)

if __name__== "__main__":
    utama()