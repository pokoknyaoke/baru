import random

angka_rahasia = random.randint(1, 10)
print('tebak angka antara 1 sampai 10!')

while True:
    tebakan = int(input('tebakan Anda: '))
    if tebakan < angka_rahasia:
        print('terlalu kecil!')
    elif tebakan > angka_rahasia:
        print ('Terlalu besar!')
    else:
        print('Benar! Anda hebat!')
        break
