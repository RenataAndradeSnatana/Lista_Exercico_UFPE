# Diconário das receitas, com as opções de comida e ingredientes:
receitas = {'hamburguer de siri': ('siri', 'pao', 'alface', 'tomate', 'queijo', 'picles'), 
             'pizza de siri': ('siri', 'trigo', 'fermento', 'ovos', 'queijo'),
             'siri frito': ('siri', 'manteiga'), 
             'siri a parmegiana': ('iri', 'trigo', 'ovos', 'queijo', 'tomate')
           }

# Diconário q vai receber o ingredientes, valor e preço:
ingredientes_qtd_preco = {'trigo': (5, 3), 'fermento': (5, 2), 'manteiga': (5,6), 
                          'ovos': (5, 2), 'batata': (5, 4), 'arroz': (5, 30),
                          'siri': (5, 8), 'pao':(5, 2), 'tomate': (5, 2),
                          'alface': (5, 1), 'picles': (5, 3), 'queijo': (5, 5)
                          }
                          
# Diconário menu, com as opções e preço:
menu = {'hamburguer de siri': 24, 'pizza de siri': 42, 'siri frio': 15, 'siri a parmegiana': 24}


valor_caixa = 40

### Código ###

receita_nova = 3 #(variável que comparara se um novo pedido foi solicitado)
valor_compra = 0 #(variável que recebera os valores dos pedidos entregue)
hambúrguer_de_siri = 0 #(variável que armazena a quantidade de hamburguer de siri mais vendido )

#(variável que armazena a quantidade de pedidos diferentes de hamburguer de siri mais vendido )
pizza_de_siri = 0 
siri_frio = 0
siri_parmegiana = 0
outros_pedidos = 0

vendas = True
while vendas != False:
     
    
        
    try:
        pedidos = input()
        if pedidos == '':
            vendas = False
            
        for cardapio in menu.keys():
            print(menu.keys())
            
            if  cardapio != pedidos:
                receita_nova = receita_nova - 1
                print('siri com fritas ainda não é uma opção disponível.')
                
                if receita_nova == 0:
                    novo_pedido = pedidos # Variável que vai receber o nome do novo pedido
                    
                    ingredientes_novo_pedido = input().split(' ')
                    novos_ing = tuple(ingredientes_novo_pedido)
                    
                    # Adicionando nas receitas e no menu a nova opção de pedido
                    receitas[novo_pedido] = novos_ing
                    menu[novo_pedido] = novos_ing
                    
                    # Verificando se há ingredientes e Subtraindo ingredientes da varíavel ingredientes_qtd_preco(estoque)
                    for item in novos_ing:
                        
                        if item in ingredientes_qtd_preco:
                            ingredientes_qtd_preco[item] = ingredientes_qtd_preco[item][0] - 1, ingredientes_qtd_preco[item][1]
                            
                            valor_compra = valor_compra + ingredientes_qtd_preco[item][1]
                            
                            print(f'Atendendo demandas, {novo_pedido} é a mais nova adição ao cardápio do Siri Cascudo.')
                                                            
                        else: # Quando o item não está em estoque (ingredientes_qtd_preco)
                            valor_caixa  = valor_caixa - ingredientes_qtd_preco[item][1]
                    
            
            elif cardapio == pedidos:
                for cardapio in novos_ing:
                        
                        if cardapio in ingredientes_qtd_preco:
                            ingredientes_qtd_preco[item] = ingredientes_qtd_preco[item][0] - 1, ingredientes_qtd_preco[item][1]
                            valor_compra = valor_compra + ingredientes_qtd_preco[item][1]
                            print(f'{pedidos} saindo...')
                        
                            if pedidos == 'hambúrguer de siri':
                                hambúrguer_de_siri = hambúrguer_de_siri + 1
                                
                            elif pedidos == 'pizza de siri':
                                pizza_de_siri =  pizza_de_siri + 1 
                            
                            elif pedidos == 'siri frio':
                                siri_frio =  siri_frio + 1  
                            
                            elif pedidos == 'siri a parmegianao':
                                siri_parmegiana =  siri_parmegiana + 1 
                            
                            elif pedidos == novo_pedido:
                                outros_pedidos = outros_pedidos + 1
                            
                        else: # Quando o item não está em estoque (ingredientes_qtd_preco)
                            valor_caixa  = valor_caixa - ingredientes_qtd_preco[item][1]
        
        vendidos = {'hambúrguer de siri': hambúrguer_de_siri, 'pizza de siri': pizza_de_siri,'siri frio': siri_frio, 'siri a parmegiana': siri_parmegiana, novo_pedido: outros_pedidos}

        mais_vendido = max(vendidos.values()), max(vendidos.keys())

        if mais_vendido[1] == 'hambúrguer de siri':
            print('O bom e tradicional hambúrguer de siri, líder em vendas, nunca será superado!')
        else:
            print(f'{mais_vendido[1].capitalize()} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri.') 

    except:
        break     


print('##### Fim do expediente #####')

print(f'O lucro obtido no dia de hoje foi de R${valor_compra}.') 


          