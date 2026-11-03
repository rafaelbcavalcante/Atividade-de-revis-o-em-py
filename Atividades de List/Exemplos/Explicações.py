numeros = [5, 3, 5, 8, 5, 2] 

valor = int(input("Número a ser contado: ")) 

qtd = 0 

cont = 0 


while cont < len(numeros): #compara se o valor de cont é menor q a quantidade de elementos na lista

    if numeros[cont] == valor: 

        qtd = qtd + 1 

    cont = cont + 1 

 

print("O número", valor, "aparece", qtd, "vez(es) na lista.") 

numeros = [7, -2, 15, 4, 9] 

maior = numeros[0] 

menor = numeros[0] 

cont = 1 

 

while cont < len(numeros): 

    if numeros[cont] > maior: 

        maior = numeros[cont] 

    if numeros[cont] < menor: 

        menor = numeros[cont] 

    cont = cont + 1 

 

print("Maior:", maior) 

print("Menor:", menor)