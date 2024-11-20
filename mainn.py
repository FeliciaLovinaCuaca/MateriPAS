import numpy as np
apb=input('Apel Budi= ')
kel=input('Kelahiran Orang = ')

if (int(apb)==kel):
    print('Tidak Bisa dibagi')
elif (int(apb)%int(kel)==0):
    print('Tidak Bisa dibagi')
else:
    print('Bisa Dibagi')