carros=[
    {'fabricante':'fiat','modelo':'palio','ano':2010,'kmrodado':120000,'preco':2300},
    {'fabricante':'fiat','modelo':'argo','ano':2018,'kmrodado':40000,'preco':50000},
    {'fabricante':'fiat','modelo':'pulse','ano':2023,'kmrodado':12000,'preco':90000},
    {'fabricante':'honda','modelo':'fit','ano':2015,'kmrodado':100000,'preco':60000},
    {'fabricante':'honda','modelo':'civic','ano':2010,'kmrodado':80000,'preco':40000},
    {'fabricante':'honda','modelo':'city','ano':2008,'kmrodado':140000,'preco':33000},
    {'fabricante':'gm','modelo':'corsa','ano':1999,'kmrodado':280000,'preco':8000},
    {'fabricante':'gm','modelo':'prisma','ano':2019,'kmrodado':15000,'preco':45000},
    {'fabricante':'toyota','modelo':'corolla','ano':2014,'kmrodado':7000,'preco':62000},
    {'fabricante':'toyota','modelo':'yaris','ano':2018,'kmrodado':5000,'preco':75000},
]

def imprimir(lista):
    print("Fabricante\tModelo\tAnoFabricacao\tKM Rodado\tPreço")
    print('----------------------------------------------------------------')
    for c in lista:
        print(f"{c['fabricante']}\t\t{c['modelo']}\t{c['ano']}\t\t{c['kmrodado']}\t\t{c['preco']}")
    print('--------------------------------------------------------------')
    
imprimir(carros) # Exibir a lista antes da ordenação

op=int(input("Escolha a opção: \n1)Fabricante \n2)modelo \n3)Ano \n4)Km Rodado \n5)Preço \n"))

if (op==1):
     ordenados = sorted(carros, key=lambda item: item['fabricante']) # Entre [] colocar o nome do que deseja ordenar
     imprimir(ordenados) # Exibir a lista após a ordenação
if (op==2):
     ordenados = sorted(carros, key=lambda item: item['modelo']) # Entre [] colocar o nome do que deseja ordenar
     imprimir(ordenados) # Exibir a lista após a ordenação
    
if (op==3):
     ordenados = sorted(carros, key=lambda item: item['ano']) # Entre [] colocar o nome do que deseja ordenar
     imprimir(ordenados) # Exibir a lista após a ordenação
    
if (op==4):
     ordenados = sorted(carros, key=lambda item: item['kmrodado']) # Entre [] colocar o nome do que deseja ordenar
     imprimir(ordenados) # Exibir a lista após a ordenação
    
if (op==5):
     ordenados = sorted(carros, key=lambda item: item['preco']) # Entre [] colocar o nome do que deseja ordenar
     imprimir(ordenados) # Exibir a lista após a ordenação
    

