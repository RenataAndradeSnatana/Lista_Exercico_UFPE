# Quantidade de pedras que serão lançadas 
quant_pedras = int(input())

# Entrada 1 dos valores das distânças em string e transformada em lista
list_numeros_str1 = input().split(' ') 

# lista1 para armazenar os valores das distânças em inteiro através do for
list_numeros_int1 = []
for i in list_numeros_str1: 
  list_numeros_int1.append(int(i))
  

# Entrada 2 dos valores das distânças em string e transformada em lista
list_numeros_str2 = input().split(' ')

# lista1 para armazenar os valores das distânças em inteiro através do for
list_numeros_int2 = []
for j in list_numeros_str2:
  list_numeros_int2.append(int(j))
 
 
# Lista com as distancia representada pelos 'indice', conforme a quantidade de pedras lançada = quant_pedras 
lista_distancia = [] 
for n in range(quant_pedras):
  lista_distancia.append(n)
      

# Transformando as listas de entrada em dicionário a partir da lista_distancia 
dic_dist_pedras_Gohan = {lista_distancia[k]: list_numeros_int1[k] for k in range(len(lista_distancia))}
dic_dist_pedras_Piccolo = {lista_distancia[k]: list_numeros_int2[k] for k in range(len(lista_distancia))}

# Verificando as distâncias dos participantes
contador = 0

for valor1 in dic_dist_pedras_Gohan.values():
    if valor1 in dic_dist_pedras_Piccolo.values():
            for chave_2 in dic_dist_pedras_Piccolo.keys():
                if valor1 == dic_dist_pedras_Piccolo[chave_2] and dic_dist_pedras_Piccolo[chave_2] != '':
                    dic_dist_pedras_Piccolo[chave_2] = ''
                    contador = contador + 1
                    break
                
       
    
if len(dic_dist_pedras_Piccolo) == contador:
      print('Dale Gohan!') 
else:
  print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.') 


print(lista_distancia)
print(list_numeros_int1)
print(list_numeros_int2)
print(dic_dist_pedras_Gohan)
print(dic_dist_pedras_Gohan.values())
print(dic_dist_pedras_Piccolo)



