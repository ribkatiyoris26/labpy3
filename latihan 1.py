print ('============== latihan 1 ======================')
print ('tampilkan bilangan acak lebih kecil dari 0,5')

import random
jumlah = int(input('masukan jumlah n: '))
print()
for i in range (jumlah):
    i=random.uniform(0.0,0.5)
    print(i)
print()
print('============== selesai ==================')
