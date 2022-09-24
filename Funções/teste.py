 
'''Crie uma função que atribua cada uma das alunas em uma das equipes da lista equipes_bootcamp_dados, de modo que 
cada equipe pode ter 3 alunas no máximo.Para isso ordene em alfabética. 
O seu resultado deve ser um dicionário python. 
exemplo {'BerthaLutz': ['Ana', 'Bruna', 'Camila'], 'GraceHopper': ['Elaine','Erika','Luiza'],... }'''

####################################################################################################################

equipes_bootcamp_dados = ['BerthaLutz', 'GraceHopper', 'JaquelineGoes', 'SarahGilbert']

lista_alunas = ['Maria', 'Ana','Camila','Mariana','Elaine','Patricia','Marina','Erica','Larissa','Luiza', 'Nicole','Bruna']
# nomes_alunas_ordem_afal = sorted(alunas)

dicionario = {}

chave = '' 
def ordenacao(lista_alunas, equipes_bootcamp_dados):
    nomes_ordem = sorted(lista_alunas)
    valor1 =nomes_ordem[0],nomes_ordem[1],nomes_ordem[2]
    valor2 =nomes_ordem[3],nomes_ordem[4],nomes_ordem[5]
    valor3 =nomes_ordem[6],nomes_ordem[7],nomes_ordem[8]
    valor4 =nomes_ordem[9],nomes_ordem[10],nomes_ordem[11]
    lista_alunos = [valor1, valor2, valor3, valor4]
    dicionario = dict(zip(equipes_bootcamp_dados, lista_alunos))
    return dicionario

print(ordenacao(lista_alunas, equipes_bootcamp_dados))
   