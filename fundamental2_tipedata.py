print('\ntipe data skalar => tipe data sederhana')
anak1 = 'Putu'
anak2 = 'Made'
anak3 = 'Komang'
anak4 = 'Ketut'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')
anak = ['Putu', 'Made', 'Komang', 'Ketut']
anak.append('Balik')
print(anak)

print('\nsapa anak ke 3')
print(f'Hai {anak[3]}')

print('\nsapa semua anak')
print(f'Hai semua {anak}')

print('\nsapa semua anak dengan for')
for a in anak:
    print(f'Hai {a}')

print('\nsapa semua anak: cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}')

