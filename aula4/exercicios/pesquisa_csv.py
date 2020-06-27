import matplotlib.pyplot as plt



def abrir():
    arquivo = open("aula4/exercicios/Pesquisa de Gostos.csv",'r')
    lista_cadastro = []
    cont=0
    for pessoa in arquivo:
        if cont == 0:
            cont += 1
            continue
        pessoa = pessoa.strip().rstrip("\"")
        #pessoa = pessoa.rstrip("\"")
        pessoa = pessoa.split('","')
        lista_cadastro.append(pessoa)
    arquivo.close()
    return lista_cadastro


# ['250', 'Edmilson', '36', 'f', 'angela_jah@hotmail.com', '023943813972']

clientes = abrir()

for i in clientes:
    print(clientes)

