print("Program menghitung Luas dan Volume Prisma Seitiga")
"""
Programer : Dewa DWi Eka Putra
Kelas : TF22A
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""

# Nilai
SisiSegitiga = 10
TinggiPrisma = 15
Alas = 4
TinggiSegitiga = 9

# Rumus

LuasSelimut = (SisiSegitiga + SisiSegitiga + SisiSegitiga) * TinggiPrisma
LuasPermukaan = LuasSelimut + Alas * TinggiSegitiga
VolumePrismaSegitiga = Alas * TinggiSegitiga * TinggiPrisma /2;

print("Luas Selimut :", LuasSelimut)
print("Luas Permukaan :", LuasPermukaan)
print("Volume Prisma Segitiga :", VolumePrismaSegitiga)