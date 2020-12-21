var1 = 'hello world'
var2 = "python programing"

print(("var1[0]: "), var1[0])
print(("var2[1:5]: "), var2[1:5])


var1 = 'hello world'

print("update string : - ", var1[:6] + 'python')

print("nama saya %s, umur saya adalah %s tahun" % ('taufiq alif rahman', 22))

print(r'C:\\taufiq')

# LATIHAN 1

txt = 'hello world'


# perintah len untuk menentukan berapa banyak karakter yang terdapat di variable
print(len(txt))
print(txt[10])  # mencari nilai paling akhir
print(txt[2:5])  # karakter ke-2 s/d ke-5
print(txt[:5] + 'world')  # menghilangkan spasi
print(txt.upper())  # merubah karakter menjadi huruf besar
print(txt.lower())  # merubah karakter menjidi huruf kecil
print(txt.replace("h", "J"))  # merubah karakter "h" menjadi karakter "J"

# LATIHAN 2

umur = 24
txt = 'hallo, nama saya john, dan umur saya adalah {} tahun'
print(txt.format(umur))
