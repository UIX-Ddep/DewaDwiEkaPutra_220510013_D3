print("Program menghitung Luas dan Volume Kerucut")
"""
Programer : Dewa DWi Eka Putra
Kelas : TF22A
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""

# Nilai
Garispelukiskerucut = 18
Jarijari = 10
Tinggikerucut = 20

# Rumus
LuasSelimut = 3.14 * Jarijari * Garispelukiskerucut
LuasPermukaan = LuasSelimut + 3.14 * Jarijari * Jarijari
VolumeKerucut = 3.14 * Jarijari * Jarijari * Tinggikerucut / 3 ;

print('Luas Selimut Kerucut :', LuasSelimut)
print("Luas Permukaan Kerucut :", LuasPermukaan)
print("Volume Kerucut:", VolumeKerucut)