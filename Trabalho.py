import os
def clear():
    os.system('cls' if os.name == 'nt' else 'else')


paises = [{'Pais' : 'China', 'Porcentagem' : 30 },
          {'Pais' : 'Indonesia', 'Porcentagem' : 10 },
          {'Pais' : 'India', 'Porcentagem' : 3 },
          {'Pais' : 'Filipinas', 'Porcentagem' : 5 },
          {'Pais' : 'Eua', 'Porcentagem' : 1 },
          {'Pais' : 'Brasil* ', 'Porcentagem' : 1 },
          'Industrias*'
]

Empresa = [{'Empresa' : 'Coca-Cola', 'Poluição' : 27.7 },
           {'Empresa' : 'PepsiCo', 'Poluição'  : 20},
           {'Empresa' : 'Nestlé', 'Poluição' : 12.73},
           {'Empresa' : 'Unilever', 'Poluição' : 10},
           {'Empresa' : 'Procter & Gamble', 'Poluição' : 8.18},
           {'Empresa' : 'Mondelez International', 'Poluição' : 7.27},
           {'Empresa' : 'Mars Incorporated', 'Poluição' : 5.45},
           {'Empresa' : 'Colgate-Palmolive', 'Poluição' : 3.64},
           {'Empresa' : 'Danone', 'Poluição' : 4.55},
           {'Empresa' : 'Perfetti van Melle', 'Poluição' : 2.73}]

Brasil = [
    {'Estado' :'São Paulo', 'Culpa' : 'São Paulo contribui significativamente para a poluição dos oceanos, principalmente devido aos resíduos industriais e urbanos, por conta de ser o estado mais industrializado e densamente povoado'},
    {'Estado' :'Rio de Janeiro', 'Culpa' : 'Rio de Janeiro é um importante contribuinte para a poluição marinha, especialmente devido à sua densa população costeira e atividades turísticas que levam ao descarte inadequado de resíduos solidos'},
    {'Estado' :'Bahia', 'Culpa' : 'Bahia possui uma extensa costa e atividades industriais relevantes, especialmente nas áreas de petróleo e gás. Essas atividades podem gerar poluentes que acabam nos oceanos, contribuindo para a poluição marinha.'},
    {'Estado' :'Pernambuco', 'Culpa' : 'Pernambuco é contribuinte significativo para a poluição dos oceanos devido aos portos e atividades industriais oque leva ao descarte inadequado de resíduos industriais e urbanos'}
]

def calc():
    clear()
    total = 150000000
    num = int(input('Digite numero de toneladas para realizarmos calculode porcetagem do mesmo com o total de toneladas no oceano'))
    final = (num/total) * 100
    print(f('f{num} equivale à {final}% da quantidade de lixo nos oceanos'))
    input('clique enter para retornar ao menu')

    

def menu():
    clear()
    print('Os principais países responsáveis pela poluição oceânica são:')
    for pais in paises:
        if isinstance(pais, dict):
            for chave, valor in pais.items():
                print(f'{chave} : {valor}')
        else:
            print(f'{pais}')
    escolha = input("Digite Brasil ou Industrias caso deseje obter mais informações sobre os mesmos, ou digite Calculo para poder fazer um cálculo da porcentagem de lixo representaria o peso colocado: ").upper()
    submenu(escolha)

def submenu(escolha):
    
    clear()
    if escolha == 'BRASIL':
        for estado in Brasil:
            print('\n')
            for chave, valor in estado.items():
                print(f'{valor}:')
        input('clique enter para retornar ao menu')
    elif escolha == 'INDUSTRIAS' or escolha == 'INDUSTRIA':
        for empresa in Empresa:
            for chave, valor in empresa.items():
                print(f'{chave} : {valor}')
        input('clique enter para retornar ao menu')
    else:
        print("Escolha inválida.")
        input('clique enter para retornar ao menu')



while True:
    print('O que deseja realizar?\n1.Ver principais paises poluentes dos oceanos\n2. Calcular porcentagem do lixo produzido em comparacao com o total de lixo nos oceanos')
    escolha = int(input('> '))
    if escolha == 1:
        menu()
    elif escolha == 2:
        calc()
    else:
        print('Escolha invalida\n')