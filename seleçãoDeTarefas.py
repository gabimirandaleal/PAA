def organizarTarefas(listaIdentificador, listaInicio, listaFim):    
    S = []
    S.append(listaIdentificador[0])
    k=0
    contTempo=listaFim[0]-listaInicio[0]
    for i in range(1, len(listaFim)):
        if listaInicio[i] >= listaFim[k]:
            if contTempo + (listaFim[i]-listaInicio[i]) <= 120:
                S.append(listaIdentificador[i])
                k=i
                contTempo = contTempo +(listaFim[i]-listaInicio[i])
    return S
    
def aux():
    tamanho = int(input())
    listaIdentificador = []
    listaInicio = []
    listaFim = []
    lista = []
    for i in range (tamanho):
        lista = input().split(' ')
        identificador = lista[0]
        inicio = int(lista[1])
        fim = int(lista[2])
        
        listaIdentificador.append(identificador)
        listaInicio.append(inicio)
        listaFim.append(fim)
    for i in range(1, len(listaFim)):
        for j in range(len(listaFim)):
            if listaFim[i]<listaFim[j]:        
                aux = listaFim[i]
                listaFim[i] = listaFim[j]
                listaFim[j] = aux
                aux = listaIdentificador[i]
                listaIdentificador[i] = listaIdentificador[j]
                listaIdentificador[j] = aux
                aux = listaInicio[i]
                listaInicio[i] = listaInicio[j]
                listaInicio[j] = aux
    S = organizarTarefas(listaIdentificador, listaInicio, listaFim)
    print(len(S))
    for i in range(len(S)):
        print(S[i])

aux()
