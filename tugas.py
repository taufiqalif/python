import os
import sys
p = print
oc = os.system
while True:
    p("")
    p("")
    c = input("A)dd, E)dit, D)elete, S)earch, L)ist, Q)uit: ")
    if c.lower() == 'q':
        break
    elif c.lower() == '1':
        i = open('database.txt', 'r').read().splitlines()
        p(" |===================================================================|")
        p(" |============================= DAFTAR ==============================|")
        p(" |===================================================================|")
        p(" |       NAMA     |     NIM     |   TUGAS   |  UTS |  UAS |  AKHIR   |")
        P(" |===================================================================|")
        for l in i:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama : ', '').replace('Nim : ', '').replace('Tugas : ', '').replace(
                    'UTS : ', '').replace('UAS : ', '').replace('Akhir : ', '')
                na, ni, tu, uts, uas, akhir = l1.strip().split('|')
                p((' | ')+(na[:15]).ljust(17, '.')+(' | ')(ni).ljust(17)+(' | ')+(tu).ljust(6)+(
                    ' | ')+(uts).ljust(6)+(' | ')+(uas).ljust(6)+(' | ')+(akhir).ljust(6)+(' | '))
        p(" |===================================================================|")
    elif c.lower() == 'd':
        u = open('database.txt', 'r').read().splitlines()
        target = input('Masukan Nama : ')
        nm = []
        for l in u:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama : ', '').replace('Nim: ', '').replace(
                    'Tugas : ', '').replace('UTS : ', '').replace('UAS : ', '').replace('Akhir : ,')
                na, ni, tu, uts, uas, akhir = l1.strip().split('|')
                if str(na) == str(target):
                    p('BERHASIL MENGHAPUS DATA %s' % (target))
                    pass
                else:
                    nm.append(str(1)+'\n')
        new = open('database.txt', '')
