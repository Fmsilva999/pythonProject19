valores = []
prods = []
alto = []
while True:
    prod = str(input('Nome do produto: ')).title().strip()
    valor = -1
    while valor < 0:
        valor = float(input('valor: R$'))
    prods.append(prod)
    valores.append(valor)
    if valor >= 1000:
        alto.append(prod)
    cond = ' '
    while cond not in 'sn':
        cond = str(input('Deseja continuar? ')).lower().strip()[0]
    if cond == 'n':
        break
print('-'*10, 'FIM DO PROGRAMA', '-'*10)
print(f'O total da compra foi de R${sum(valores):.2f}')
print(f'Temos {len(alto)} produto(s) custando mais de R$1000. {alto}')
print(f'O produto mais barato foi {prods[valores.index(min(valores))]} que custa R${min(valores):.2f}')