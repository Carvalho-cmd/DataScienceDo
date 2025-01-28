num = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
dez = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove']
vin = ['vinte']

final = {}

for i in range(30):
    if i < 10:
        final[i] = num[i]
    elif i >= 10 and i < 20:
        d = i - 10
        final[i] = dez[d]
    else:
        v = i - 20
        if v == 0:
            final[i] = vin[0]
        else:
            valor = f'{vin[0]} e {num[v]}'
            final[i] = valor

print(final)