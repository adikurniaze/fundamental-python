# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL: Eksekusi berurutan
print('Hello World')
print('by Adi')
print('Tanggal 27 Juni 2020')
print('-' * 10)

# PERCABANGAN: Eksekusi terpilih

ingin_cepat = True
if ingin_cepat:
    print('jalan lurus kedepan!')
else:
    print('jalan lain')

# PERULANGAN
jumlah_anak = 4

for index_anak in range(1, jumlah_anak+1): # jumlah perulangan
    print(f'Halo anak #{index_anak}')
