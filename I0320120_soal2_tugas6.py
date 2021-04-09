# masukan nilai fisika Raini
nilai_pertama = int(input('Masukkan nilai fisika pertama Raini: '))
nilai_kedua = int(input('Masukkan nilai fisika kedua Raini: '))
nilai_ketiga = int(input('Masukkan nilai fisika ketiga Raini: '))
nilai_keempat = int(input('Masukkan nilai fisika keempat Raini: '))

print('----------------------------------------')

nilai = [nilai_pertama, nilai_kedua, nilai_ketiga, nilai_keempat]
awalan = 0
for x in range(1, 5):
    print("nilai ke-%d Raini adalah" % x, nilai[awalan])
    awalan += 1

print('----------------------------------------')

nilai_keseluruhan = (nilai_pertama + nilai_kedua + nilai_ketiga + nilai_keempat)
print("total nilai keseluruhan Raini adalah", nilai_keseluruhan)
nilai_ratarata = int(nilai_keseluruhan / 4)
print("rata-rata nilai Raini adalah", nilai_ratarata)
print()