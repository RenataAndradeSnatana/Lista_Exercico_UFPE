registro_pokemon = {}

while True:  
      
    try:
        entrada = input().split()
    
        for i in entrada:
            if i == 'ADD':
              if entrada[1] in registro_pokemon.keys():
                  print('Pokémon já adicionado na Pokédex')
              else:
                  descricao = input()
                  registro_pokemon[entrada[1]] = descricao
                  print('Pokémon adicionado com sucesso')
                  
            elif i == 'DESC':
               if entrada[1] not in registro_pokemon.keys():
                  print('Ainda não há registro desse Pokémon')
                
               else:
                  print(registro_pokemon[entrada[1]])
                
       
    except:
        break