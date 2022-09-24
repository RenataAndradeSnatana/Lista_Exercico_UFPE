viloes = {'Vingador': 30, 'Tiamat': 20, 'Vingador das Sombras': 14, 'outros adversários': 9}

# Dicionario que contém as armas e armaduras dos heróis
instrumento_luta = {'chifre': 2, 'cajado': 4, 'espada': 6, 'grande espada': 8, 'dardo': 12,
                    'armadura pesada': 0, 'armadura media': 1, 'armadura leve': 3}

grupo = {'Bobby': ('grande espada', 'armadura media'), 'Diana': ('dardo', 'armadura leve'),
         'Eric': ('grande espada', 'armadura pesada'), 'Hank': ('espada', 'armadura media'),
         'Presto': ('cajado', 'armadura leve'), 'Sheila': ('espada', 'armadura leve'),
         'Uni': ('chifre', 'armadura leve')}

# Código
vilao = input()
turnos = int(input())

nome_vilao = vilao

if vilao != 'Vingador' and vilao != 'Tiamat' and vilao != 'Vingador das Sombras':
    vilao = 'outros adversários'

poder_vilao = viloes[vilao]

while turnos > 0:
    if poder_vilao > 0:
        personagem = input()

        if personagem != 'Mestre dos Magos':
            arma, armadura = grupo[personagem]
            armadura, valor = instrumento_luta[armadura], instrumento_luta[arma]

            poder_vilao = poder_vilao - valor
            turnos = turnos - armadura -1

        else:
            print('Muito obrigado amigo, que nos vejamos novamente um dia')
            exit()
    else:
        break

if poder_vilao <= 0:
    print(f'{personagem} executou o ultimo golpe em {nome_vilao}, estamos livres!')
elif poder_vilao >= 0:
    print(f'Oh nao, {nome_vilao} e muito forte, este e o fim!')


