n = 0
nm = []
nim = []
tugas = []
uts = []
uas = []
akhir = []

while True:
    nama = input("Nama      :")
    nm.append(nama)
    Nim = input("NIM       :")
    nim.append(Nim)
    Tugas = input("Tugas     :")
    tugas.append(Tugas)
    Uts = input("UTS       :")
    uts.append(Uts)
    Uas = input("UAS       :")
    uas.append(Uas)
    Akhir = (int(Tugas) * .30) + (int(Uts) * .35) + (int(Uas) * .35)
    akhir.append(Akhir)

    data = ' '
    while data != 'Y' and data != 'T':
        data = input("Tambah data [Y/T] ?")

    n += 1
    if data == 'T':
        break

print("======================================================================")
print(" NO  |   NAMA    |    NIM      |   TUGAS   | UTS   |   UAS   |  AKHIR ")
print("======================================================================")

for a in range(n):
    print(" ", a+1, " | ", nm[a],  "  |  ", nim[a], "  |  ", tugas[a],"  |  ", uts[a],  "  |  ", uas[a], "  |  ", akhir[a], "|")

print("======================================================================")
