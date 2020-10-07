def organizarTarefas(listaIdentificador, listaPeso, listaValor, tamanhoDaMochila):
    capacidadePreenchida = 0
    porcentagem = []
    identificador = []
    i = 0
    while capacidadePreenchida != 100:
        if ((listaValor[i]*100)/tamanhoDaMochila)+capacidadePreenchida <= 100:
            porcentagem.append(100.0)
            identificador.append(listaIdentificador[i])
            capacidadePreenchida += (listaValor[i]*100)/tamanhoDaMochila
        else:
            quantoFalta = int(100-capacidadePreenchida)
            aux = (listaValor[i]*100)/tamanhoDaMochila
            porcentagem.append(round(quantoFalta*100/aux, 2))
            identificador.append(listaIdentificador[i])
            capacidadePreenchida = 100
        i=i+1
    print(len(porcentagem))
    for i in range(len(porcentagem)):
        print(identificador[i], porcentagem[i])
    
def aux():
    tamanho = int(input())
    listaIdentificador = []
    listaValor = []
    listaPeso = []
    lista = []
    for i in range (tamanho):
        lista = input().split(' ')
        identificador = lista[0]
        valor = int(lista[1])
        peso = int(lista[2])

        listaIdentificador.append(identificador)
        listaValor.append(valor)
        listaPeso.append(peso)
        if peso/valor > listaPeso[i-1]/listaValor[i-1]:
            aux = peso
            listaPeso[i] = listaPeso[i-1]
            listaPeso[i-1] = aux
            aux = identificador
            listaIdentificador[i] = listaIdentificador[i-1]
            listaIdentificador[i-1] = aux
            aux = valor
            listaValor[i] = listaValor[i-1]
            listaValor[i-1] = aux
    for i in range(1, len(listaPeso)):
        for j in range(len(listaPeso)):
            if listaPeso[i]/listaValor[i]>listaPeso[j]/listaValor[j]:        
               aux = listaPeso[i]
               listaPeso[i] = listaPeso[j]
               listaPeso[j] = aux
               aux = listaIdentificador[i]
               listaIdentificador[i] = listaIdentificador[j]
               listaIdentificador[j] = aux
               aux = listaValor[i]
               listaValor[i] = listaValor[j]
               listaValor[j] = aux
    tamanhoDaMochila = int(input())
    organizarTarefas(listaIdentificador, listaPeso, listaValor, tamanhoDaMochila)

aux()

