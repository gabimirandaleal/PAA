def mergeSort(tamanho, lista):
    tamanho = len(lista)
    if tamanho > 1:
        meio = int(tamanho/2)
        esquerda = mergeSort(tamanho, lista[:meio])
        direita = mergeSort(tamanho, lista[meio:])
        resultado = []
        while len (esquerda) > 0 and len(direita) > 0:
            if esquerda[0] < direita[0]:
                resultado.append(esquerda[0])
                esquerda.pop(0)
            else:
                resultado.append(direita[0])
                direita.pop(0)
        for i in esquerda:
            resultado.append(i)
        for i in direita:
            resultado.append(i)
        return resultado
    else:
        return lista

def aux():
    tamanho = int(input())
    lista = []
    for i in range (tamanho):
        valor = int(input())
        lista.append(valor);
    lista = mergeSort(tamanho, lista)
    print(tamanho)
    for i in range (tamanho):
        print(lista[i])
aux()
