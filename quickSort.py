def quickSort(tamanho, lista):
    quickSort2(lista, 0, len(lista)-1)

def quickSort2(lista, inicio, fim):
    if inicio < fim:
        p = particao(lista, inicio, fim)
        quickSort2(lista, inicio, p-1)
        quickSort2(lista, p+1, fim)
        
def particao(lista, inicio, fim):
    pivoValor = lista[inicio]
    esquerda = inicio+1
    direita = fim

    done = False
    
    while not done:
        while esquerda <=direita and lista[esquerda] <= pivoValor:
            esquerda = esquerda + 1
        while lista[direita] >= pivoValor and direita >= esquerda:
            direita = direita - 1
        if direita < esquerda:
            done = True
        else:
            temp = lista[esquerda]
            lista[esquerda] = lista[direita]
            lista[direita] = temp
    temp = lista[inicio]
    lista[inicio] = lista [direita]
    lista[direita] = temp
    return direita

def aux():
    tamanho = int(input())
    lista = []
    for i in range (tamanho):
        valor = int(input())
        lista.append(valor);
    quickSort(tamanho, lista)
    print(tamanho)
    for i in range (tamanho):
        print(lista[i])
    
aux()
