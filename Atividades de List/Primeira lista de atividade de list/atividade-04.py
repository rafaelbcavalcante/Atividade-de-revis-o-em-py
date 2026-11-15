notas = [7.5, 4.0, 9.0, 5.5, 8.0, 6.0]
cont=0
qtmaior6=0
while cont < len(notas):
    if notas[cont] >= 6:
        print(f'posição nota maior: {cont}')
        qtmaior6=qtmaior6+1
    cont=cont +1
print(f'Quantidade de notas q foram maiores q 6: {qtmaior6}')