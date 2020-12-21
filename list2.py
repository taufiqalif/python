#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:08:25 2020

@author: taufiq
"""

# Membuat list kosong untuk menampung hobi
data = []
stop = False
i = 0

# Mengisi hobi
while(not stop):
    nama = input("masukan nama : ")
    data.append(nama)
    nim = input("NIM : ")
    data.append(nim)
    tugas = input("nilai tugas: ")
    data.append(tugas)
    uts = input("nilai UTS: ")
    data.append(uts)
    uas = input("nilai UAS: ")
    data.append(uas)
   

    # Increment i
    i += 1
    
    tanya = input("Tambah data (y/t): ")
    if(tanya == "t"): 
        stop = True


# Cetak Semua Hobi
print ("=" * 50 )
print ("no |", "nama |", "nim |", "tugas |", "UTS |", "UAS |")
print("=" * 50)
for hb in data:
    print ("{}".format(hb))
print("=" * 50)