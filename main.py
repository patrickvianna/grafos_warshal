from vertice import Vertice
rotuloVertices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]
# arrayVertices = []

def main():
    arrayVertices = GetNumeroVertices()
    arrayVertices = GetVerticesIncidentes(arrayVertices)

    decisaoMenu = 1
    while decisaoMenu != 0:
        decisaoMenu = Menu()
        if decisaoMenu == 1:
            PrintListaAdjacencia(arrayVertices)
        elif decisaoMenu == 2:
            PrintMatrizAdjacencia(arrayVertices)
        # elif decisaoMenu == 3:
        #     PrintCaminhosA(arrayVertices)

def GetVerticesIncidentes(lista):
    for v in lista:
        incidentes = input("Quais são os vertices incidentes para o Vertice: < " + v.rotulo + " >: ")
        arrayIncidentes = incidentes.split(",")
        v.incidentes = FindVerticesIncidentes(lista, arrayIncidentes)

    return lista

def FindVerticesIncidentes(lista, incidentes):
    retorno = []
    for i in incidentes:
        match = GetVerticeByRotulo(lista, i)
        retorno.append(match)
    
    return retorno

def GetVerticeByRotulo(lista, rotulo):
    for v in lista:
        if v.rotulo.lower() == rotulo.lower():
            return v

def GetNumeroVertices():
    numeroVertices = int(input("Quantos vértices tem o seu grafo?"))
    vertices = CriaVertices(numeroVertices)
    return vertices
    # PrinArrayVertices(arrayVertices)

def CriaVertices(numeroVertices):
    verticesLst = []
    i = 0
    while i < numeroVertices:
        vertice = Vertice(i, rotuloVertices[i])
        verticesLst.append(vertice)
        i += 1

    return verticesLst

def PrinArrayVertices(lista):
    i = 0 
    print("")
    print("__ IMPRIMINDO ARRAY DE VERTICES __")
    while i < len(lista):
        print ("Posicao: " + str(lista[i].posicao) + "\t Rotulo: " + str(lista[i].rotulo))
        print ("Incidentes: [ " + str(len(lista[i].incidentes)) + " ]")
        i += 1

def PrintListaAdjacencia(lista):
    PularLinhas()
    for v in lista:
        print (str(v.rotulo) + " : ", end = '')

        i = 0
        tamanhoArrayIncidentes = len(v.incidentes)
        while i < tamanhoArrayIncidentes:
            print (str(v.incidentes[i].rotulo), end = '')
            if(i != tamanhoArrayIncidentes - 1):
                print(" -> ", end = '')
            i += 1
        print("")

def PrintMatrizAdjacencia(lista):
    PularLinhas()
    linha = 0
    size = len(lista)
    
    while linha < size:
        coluna = 0
        incidentesArray = lista[linha].incidentes

        while coluna < size :
            if ExisteIncidenteByPosicao(incidentesArray, coluna):
                print("1", end="")
            else:
                print("0", end="")
            print("\t", end="")
            coluna += 1

        linha += 1
        print("")

def ExisteIncidenteByPosicao(lista, posicao):
    for v in lista:
        if v.posicao == posicao:
            return True
    return False

# def PrintCaminhosA(lista):
#     size = len(lista)
#     A = GetA(lista)
    
#     i = 0
#     Aaux = A
#     while i in i < size:
#         j = 0
#         while j < size:
#             lista
#         MultiplicaMatrizA()

# def MultiplicaMatrizA(lista):
#     size = len(lista)
#     linha = 0
#     arrayA = []
#     while linha < size:
#         coluna = 0
#         arrayAux = []
#         while coluna < size:
            


# def GetA(lista):
#     linha = 0
#     size = len(lista)
#     arrayA = []

#     while linha < size:
#         coluna = 0
#         incidentesArray = lista[linha].incidentes

#         while coluna < size :
#             linhaArrayA = []
#             if ExisteIncidenteByPosicao(incidentesArray, coluna):
#                 linhaArrayA.append(1)
#             else:
#                 linhaArrayA.append(0)
#             arrayA.append(linhaArrayA)
#             coluna += 1

#         linha += 1  
    
#     return arrayA

def PularLinhas():
    print("\n\n\n\n\n\n")

def Menu():
    print("\n___ MENU ___\n")
    decisao = int(    input("1: Imprimir lista de adjacencia\n" +
                            "2: Imprimir matriz de adjacencia\n" +
                            
                            "0: Sair\n"))
# "3: Imprimir caminhos da matriz\n" +
#                             "4: Imprimir R\n"+                            
    return decisao                        

if __name__ == "__main__":
    main()
    

