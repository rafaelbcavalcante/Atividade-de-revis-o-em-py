listaAlunos = ['Ana', 'Beto', 'Carla', 'Davi', 'Edu', 'Fabi'] 
listaNotas = [7.5, 4.0, 9.0, 5.5, 8.0, 6.0] 
listaAprovados= []
cont=0
aprovados=0
while cont < len(listaAlunos):
    print(f'Posição: {cont} - {listaAlunos[cont]} tirou {listaNotas[cont]}') #o cont mostra a posição e o listanotas o aluno q tirou a respectiva nota
    if listaNotas[cont] >= 6: #analisa se o conteúdo da lista nesse índice é maior q 6
        aprovados=aprovados+1
        listaAprovados.append(listaAlunos[cont]) #adiciona na lista de aprovvados o aluno q tirou mais q 6
    cont=cont+1
print(f'qt Aprovados: {aprovados}')
print(f'alunos Aprovados: {listaAprovados}')