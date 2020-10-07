def encherMochila(n, listaIdentificador, listaPeso, listaValor, listaAux, tamanhoDaMochila):
    K = [[0 for x in range(tamanhoDaMochila+1)] for x in range(n+1)]
 
    for i in range(n+1):
        for w in range(tamanhoDaMochila+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif listaValor[i-1] <= w:
                K[i][w] = max(listaPeso[i-1] + K[i-1][w-listaValor[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    i = n
    j = tamanhoDaMochila
    k = 0
    prod=[]
    index=[]
    ident = []
    while K[i][j] > 0:
        if K[i-1][j] != K[i][j]:
            ident.append(listaIdentificador[listaPeso.index(listaPeso[i-1])])
            j = j - listaValor[i-1] 
        i = i-1
        ident.reverse()
    return ident


def aux():
    tamanho = int(input())
    listaIdentificador = []
    listaValor = []
    listaPeso = []
    lista = []
    listaAux = []
    for i in range (tamanho):
        lista = input().split(' ')
        identificador = lista[0]
        valor = int(lista[1])
        peso = int(lista[2])
        listaAux.append(int(0))
        listaIdentificador.append(identificador)
        listaValor.append(valor)
        listaPeso.append(peso)
    tamanhoDaMochila = int(input())
    qntItens = 0
    resul = encherMochila(tamanho-1, listaIdentificador, listaPeso, listaValor, listaAux, tamanhoDaMochila)
    print(len(resul))
    for i in range(len(resul)):
        print(resul[i])
aux()

