# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
i=a=b=c=0
nama=[]
npm=[]
kls=[]
jur=[]
ang=[]
while True:
	print("masukan data ke - ',i+1")
    nama.append input("Nama anda :")
    npm.append input("npm anda :")
    if len (npm[i])=0:
    	print("npm salah")
        print
        nama.pop(i)
        npm.pop(i)
        continue
    kls.append(input("kelas anda :"))
    if len (kls[i])!=5:
    	print("kelas salah")
        print
        nama.pop(i)
        npm.pop(i)
        kls.pop(i)
        continue
    jur.append(kls[i][1:3])
    ang.append(ang[i][3:5])
    if jur[i]=='1A':
    	jur[i]='teknik informatika'
        a+=1
    elif jur[i]=='1B':
    	 jur[i]='teknik industri'
         b+=1
    elif jur[i]=='1C':
    	 jur[i]='teknik mesin'
         c+=1
    else:
    	print("kelas salah")
        print
        continue
    lagi="
    while lagi !='y' and lagi!='t':
    	lagi=input("input lagi Y/T: ")
        i+=1
    if kagi=='t':
    	break
    print("===============daftar mahasiswa===============")
    print("=" *45)
    print("no	|	nama	|	npm	|	kelas	| 	angkata	|	|	jurusan")
    print("=" *45)
    for n in range(i):
    	print(n+i,'',nama[n],'',npm[n],'',ang[n],'',jur[n]")
        