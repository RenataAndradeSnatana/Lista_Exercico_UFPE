
silabas_detectada= []

silaba_nome_hospital = ['shi', 'chi', 'ko', 'ku', 'ya', 'ma']


def divisor_silabas(palavras):
    conjunto_silabas = []
    consoantes = ''
    for i in palavras: # Pecorre casa letra da palavra
        if i in ['a','e','i','o','u']: # Verifica se a letra está contida nesta lista das vogais
            consoantes = consoantes + i # Se for a variável consoante vai receber consonate + a vogal
            conjunto_silabas.append(consoantes) # Esse junção consoante + vogal será adiconada na lista conjunto_silabras
            consoantes = '' # Esse código serve para apagar a última consoante alimentada nessa variável consoantes, deixando ela vazia
        
        else:
            consoantes = consoantes + i  # Caso o i(letra) for um letra consoante a variável recebe a consoantes vazia + i(que é a letra consoante)
    
    return conjunto_silabas

def comparando_silabas(conjunto_silabas):
    silibas_encontrada = []
    for j in conjunto_silabas:
        if j in silaba_nome_hospital:
            silibas_encontrada.append(j)
            silaba_nome_hospital.remove(j)
                
    return silibas_encontrada
  

while len(silabas_detectada) != 6:
  palavras = input()
  
  conjunto_silabas = divisor_silabas(palavras)

  silibas_encontrada = comparando_silabas(conjunto_silabas)

  #verificando a ordem
  ordem = False
  if len(conjunto_silabas) == len(silibas_encontrada):
    if palavras in 'shichikokuyama':
      ordem = True


  #add as silabas lembradas da palavra asilabas lembradas
  for j in silibas_encontrada:
    silabas_detectada.append(j)
  

  silabas_detectada_normal = ', '.join(silibas_encontrada)
  
  #prints
  if ordem == True and len(conjunto_silabas) > 1:
    print(f'A palavra {palavras} está toda no nome do hospital. Acertou em cheio, Totoro!')

  elif len(silibas_encontrada) == 0:
    print('Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.')

  elif  len(silibas_encontrada) == 1:
    print(f'Lembrei! A sílaba {silabas_detectada_normal} está no nome do hospital. Obrigada, Totoro!')

  elif  len(silibas_encontrada) > 1:
    print(f'Lembrei! As sílabas: {silabas_detectada_normal} estão no nome do hospital. Obrigada, Totoro!')

print('Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!')
