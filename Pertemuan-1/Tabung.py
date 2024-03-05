print("Program menghitung Luas dan Volume Tabung")
"""
Programer : Dewa DWi Eka Putra
Kelas : TF22A
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""

# Nilai
Jarijari = 10
TinggiTabung = 20

# Rumus 
LuasSelimutTabung = 2*3.14 * Jarijari * TinggiTabung  
LuasPermukaanTabung = LuasSelimutTabung + 2*3.14 * Jarijari * Jarijari
VolumeTabung = 3.14 * Jarijari * Jarijari * TinggiTabung

print("Luas Selimut Tabung :", LuasSelimutTabung)
print("Luas Permukaan Tabung :", LuasPermukaanTabung)
print("Volume Tabung :", VolumeTabung)

