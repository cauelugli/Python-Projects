####################################################################
#   walking.py Project
#
#   ordem: Poka, XXX, XXX, XXX, XXX
#
#   version: 0_0_0    edit: 16_04_2020
####################################################################
olhos = True
consegue_falar = True
moto = 'XT 660'

def falar():
    if consegue_falar:
        print('\n"Caralho! Olha ali uma', moto, '!!"')

def andar_na_rua():
    if olhos:
        if moto == 'Biz 125':
            pass
        if moto == 'Fan 160':
            pass
        if moto == 'XT 660':
            falar()

andar_na_rua()
