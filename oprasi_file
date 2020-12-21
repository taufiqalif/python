# input output file

# w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan dibuatkan otomatis
# r = read mode only / hanya bisa baca
# a = appeding mode / menambahkan data di akhir baris
# r+ = write and read mode


# membuat file text
file = open("data.txt",'w')
file.write("ini adalah data text yang dibuat")
file.write("\nini adalah baris kedua")
file.write("\nini adalah baris ketiga")
file.write("\nini adalah baris keempat")

file.close()

# membaca file text
file2 = open("data.txt",'r')

print(file2.read())
#print(file2.readline())

file2.close()

# appending mode

file3 = open("data.txt",'a')
file3.write("\nbaris ini menggunakan mode append")

file3.close()