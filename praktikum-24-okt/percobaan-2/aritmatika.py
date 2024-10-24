def memecah_input(perhitungan):
    hitungan = perhitungan.split(' ')
    angka1 = int(hitungan[0])
    operator = hitungan[1]
    angka2 = int(hitungan[2])
    return angka1, operator, angka2


def penambahan(angka1, angka2):
    return angka1 + angka2


def pengurangan(angka1, angka2):
    return angka1 - angka2


def perkalian(angka1, angka2):  
    return angka1 * angka2


def pembagian(angka1, angka2):
    return angka1 / angka2

def modulo(angka1, angka2):
    return angka1 % angka2

def pangkat(angka1, angka2):
    return angka1 ** angka2