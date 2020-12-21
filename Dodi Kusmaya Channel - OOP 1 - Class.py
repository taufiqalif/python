# Nama Kelas : Orang
# Properties : Nama, Tempat Lahir, Tanggal Lahir, Gender
# Method     : _get() --> Untuk mengambil nilai dari properties
# _set() --> Untuk memberikan nilai pada properties

class _mahasiswa():
    def __init__(self, nama, nim, tugas, uts, uas,):
        self.nama = nama
        self.nim = nim
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def _set(self, nama, nim, tugas, uts, uas):
        self.nama = nama
        self.nim = nim
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def _get(self):
        pass


# Memanggil Kelas
p1 = _mahasiswa('', '', '', '', '')

arr_nama = []
arr_nim = []
arr_tugas = []
arr_uts = []
arr_uas = []

print('====================================================')
print('                    Nilai Mahasiswa                 ')
print('====================================================')
print('Menu Utama :')
print('[T]ambahkan Data')
print('[R]ead Data')
print('[U]pdate Data')
print('[D]elete Data')
print('[V]iew Data')

lagi = True
while lagi:
    pilih = input('Input Pilihan [T/R/U/D/V] : ')
    if pilih in ('Tt'):
        _nama = input('Nama Lengkap               : ')
        _nim = input('Masukan NIM               : ')
        _tugas = input('Nilai Tugas            : ')
        _uts = input('Nilai UTS               : ')
        _uas = input('Nilai UAS             : ')

        p1._set(_nama, _nim, _tugas, _uts, _uas)

        arr_nama.append(p1.nama)
        arr_nim.append(p1.nim)
        arr_tugas.append(p1.tugas)
        arr_uts.append(p1.uts)
        arr_uas.append(p1.uas)
    elif pilih in ('Rr'):
        _nama = input('Nama Lengkap               : ')
        if arr_nama.count(_nama) > 0:
            _idx = arr_nama.index(_nama)
            p1._get()
            p1.nim = arr_nim[_idx]
            p1.tugas = arr_tugas[_idx]
            p1.uts = arr_uts[_idx]
            p1.uas = arr_uas[_idx]

            print('NIM                        :', p1.nim)
            print('Nilai Tugas                :', p1.tugas)
            print('Nilai UTS                  :', p1.uts)
            print('Nilai UAS                  :', p1.uas)
        else:
            print('Data tidak ditemukan.')
    elif pilih in ('Uu'):
        _nama = input('Nama Lengkap               : ')
        if arr_nama.count(_nama) > 0:
            _idx = arr_nama.index(_nama)
            _nim = input('NIM               : ')
            _tugas = input('Nilai Tugas     : ')
            _uts = input('Nilai UTS         : ')
            _uas = input('Nilai UAS         : ')

            p1._set(_nama, _nim, _tugas, _uts, _uas)
            arr_nim[_idx] = p1.nim
            arr_tugas[_idx] = p1.tugas
            arr_uts[_idx] = p1.uts
            arr_uas[_idx] = p1.uas
        else:
            print('Data tidak ditemukan.')

    elif pilih in ('Dd'):
        _nama = input('Nama Lengkap               : ')
        if arr_nama.count(_nama) > 0:
            _idx = arr_nama.index(_nama)
            arr_nama.pop(_idx)
            arr_nim.pop(_idx)
            arr_tugas.pop(_idx)
            arr_uts.pop(_idx)
            arr_uas.pop(_idx)
        else:
            print('Data tidak ditemukan.')
    elif pilih in ('Vv'):
        print('=========================================================')
        print('          NAMA          |          TTL          | GENDER ')
        print('=========================================================')
        for x in range(len(arr_nama)):
            print('%-25s%-25s%3s' %
                  (arr_nama[x], arr_nim[x], arr_tugas[x], arr_uts[x], arr_uas[x]))
        print('=========================================================')
    else:
        print('Pilihan Salah, Silakan pilih lagi [T/R/U/D/V] !')

    print()
    lagi = input('Input Data Lagi [Y/T] : ')
    while lagi not in ('YyTt'):
        lagi = input('Input Data Lagi [Y/T] : ')

    if lagi in ('Tt'):
        lagi = False
