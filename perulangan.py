baris = 10
kolom = baris
for i in range(baris):
    for j in range(kolom):
        tambahkan = i+j
        print("{0:>5}".format(tambahkan), end="")
    print()
