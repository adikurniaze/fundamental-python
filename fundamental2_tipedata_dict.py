'''
tipe data dictionary sekedar menghubungkan antara
key dan value (KVP / Key Value Pair)
'''

kamus = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(f'\n{kamus}')
print(kamus['ayah'])
print(kamus['ibu'])

print('data ini dikirimkan oleh server Gojek untuk memberikan info di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-06-27',
    'driver_list': [{'nama': 'Putu', 'jarak': 100},
                    {'nama': 'Made', 'jarak': 200},
                    {'nama': 'Komang', 'jarak': 300},
                    {'nama': 'Ketut', 'jarak': 400}
                    ]
}
print(data_dari_server_gojek)
print(f"driver sekitar ini{data_dari_server_gojek['driver_list']} ")
print(f"driver #1 {data_dari_server_gojek['driver_list'][3]}")
print(f"driver #2 {data_dari_server_gojek['driver_list'][1]['nama']} meter")
print(f"driver #2 nama: {data_dari_server_gojek['driver_list'][1]['nama']} dan jarak: {data_dari_server_gojek['driver_list'][1]['jarak']} meter")
