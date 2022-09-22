erro = False
entrada = input().split(' ')

#Transformando a entrada em lista numerica
entrada_numerica = []
for i in entrada:
  numero = int(i)
  entrada_numerica.append(numero)
  
frase = ''

def uniao_letra(letra, frase):
   frase += letra
   return frase
   
for n in entrada_numerica:
  if n >= 0 and n <= 25:
    letra = chr(n + 97)
    
  elif n > 25 and n < 50:
    letra = chr(n + 71)
    
  elif n >= 50 and n <= 75:
    letra = chr(n + 15)
     
  elif n > 75 and n <= 99:
    letra = chr(n - 11)
    
  elif n == 100:
    letra = ' '
  
  elif n > 100:
    erro = True
    

  frase = uniao_letra(letra, frase)
if erro == False:
  print(frase)
else:
  print('Infelizmente os números nao dizem nada')
  

    
   