nomes = ["Ana", "Beto", "Carla", "Davi"]
nome= input('Digite o nome:')
if nome in nomes: #utiliza a função 'in' para analisar se o conteúdo da variável nome está dentro da lista nome
    nomes.remove(nome) #remove o valor da variável presente na lista nomes
    print(f'{nome} removido')
    print(f'lista: {nomes}')
else:
    print('nome não encontrado')