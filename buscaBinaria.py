def buscaBinaria(lista, valor):
    inicio = 0
    fim = len(lista)-1
    verifica = False
    while inicio <=fim and not verifica:
        meio = int((inicio+fim)//2)
        if lista[meio] == valor:
            verifica=True
        else:
            if valor<lista[meio]:
                fim = meio-1
            elif valor > lista[meio]:
                inicio = meio+1
                
    if(verifica):
        print ("SIM")
        print (meio)
    else:
        print ("NAO")
        print (-1)
    return verifica

def aux():
    tamanho = int(input())
    lista = []
    for i in range (tamanho):
        valor = int(input())
        lista.append(valor);
    valorASerEncontrado = int(input())
    buscaBinaria(lista, valorASerEncontrado)
aux()
