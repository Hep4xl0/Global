import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

paises = [
    {'Pais': 'China', 'Porcentagem': 30},
    {'Pais': 'Indonesia', 'Porcentagem': 10},
    {'Pais': 'India', 'Porcentagem': 3},
    {'Pais': 'Filipinas', 'Porcentagem': 5},
    {'Pais': 'EUA', 'Porcentagem': 1},
    {'Pais': 'Brasil*', 'Porcentagem': 1},
    
]

empresas = [
    {'Empresa': 'Coca-Cola', 'Poluicao': 27.7},
    {'Empresa': 'PepsiCo', 'Poluicao': 20},
    {'Empresa': 'Nestlé', 'Poluicao': 12.73},
    {'Empresa': 'Unilever', 'Poluicao': 10},
    {'Empresa': 'Procter & Gamble', 'Poluicao': 8.18},
    {'Empresa': 'Mondelez International', 'Poluicao': 7.27},
    {'Empresa': 'Mars Incorporated', 'Poluicao': 5.45},
    {'Empresa': 'Colgate-Palmolive', 'Poluicao': 3.64},
    {'Empresa': 'Danone', 'Poluicao': 4.55},
    {'Empresa': 'Perfetti van Melle', 'Poluicao': 2.73}
]

brasil = [
    {'Estado': 'São Paulo', 'Culpa': 'São Paulo contribui significativamente para a poluição dos oceanos, principalmente devido aos resíduos industriais e urbanos, por conta de ser o estado mais industrializado e densamente povoado'},
    {'Estado': 'Rio de Janeiro', 'Culpa': 'Rio de Janeiro é um importante contribuinte para a poluição marinha, especialmente devido à sua densa população costeira e atividades turísticas que levam ao descarte inadequado de resíduos sólidos'},
    {'Estado': 'Bahia', 'Culpa': 'Bahia possui uma extensa costa e atividades industriais relevantes, especialmente nas áreas de petróleo e gás. Essas atividades podem gerar poluentes que acabam nos oceanos, contribuindo para a poluição marinha.'},
    {'Estado': 'Pernambuco', 'Culpa': 'Pernambuco é contribuinte significativo para a poluição dos oceanos devido aos portos e atividades industriais o que leva ao descarte inadequado de resíduos industriais e urbanos'}
]

def calcular_porcentagem():
    clear()
    total_oceanos = 150000000  # toneladas
    num = float(input('Digite o número de toneladas para calcular a porcentagem em relação ao total de lixo nos oceanos: '))
    porcentagem = (num / total_oceanos) * 100
    print(f'{num} toneladas equivalem a {porcentagem}% da quantidade total de lixo nos oceanos ({total_oceanos} toneladas)')
    input('Pressione Enter para retornar ao menu.')

def exibir_info_brasil():
    clear()
    print('Principais estados brasileiros contribuindo para a poluição marinha e a causa de sua contribuição:')
    for estado in brasil:
        print('')
        for chave, valor in estado.items():
            if chave == 'Estado':
                print(f'{valor}: ', end='')
            else:
                print(f'{valor}')
    input('Pressione Enter para retornar ao menu.')

def exibir_info_paises():
    clear()
    print('Os principais países responsáveis pela poluição oceânica são:')
    for item in paises:
        if isinstance(item, dict):
            for chave, valor in item.items():
                if chave == 'Pais':
                    print(f'{valor}: ', end='')
                elif chave == 'Porcentagem':
                    print(f'{valor}%', end=' | ')
        else:
            print(item)
    input('Pressione Enter para retornar ao menu.')

def exibir_info_empresas():
    clear()
    print('As principais empresas responsáveis pela poluição oceânica são:')
    for item in empresas:
        if isinstance(item, dict):
            for chave, valor in item.items():
                if chave == 'Empresa':
                    print(f'{valor}: ', end='')
                elif chave == 'Poluicao':
                    print(f'{valor}%', end=' | ')
        else:
            print(item)
    input('Pressione Enter para retornar ao menu.')

def menu():
    clear()
    print('O que deseja realizar?\n1. Ver os principais países poluentes dos oceanos.\n2. Ver os principais estados brasileiros poluentes dos oceanos e o motivo para isso.\n3. Ver as principais empresas poluentes dos oceanos.\n4. Calcular a porcentagem do lixo produzido em comparação com o total de lixo nos oceanos.\n5. Sair do programa.')
    escolha = input('> ')
    return escolha

while True:
    opcao = menu()
    if opcao == '1':
        exibir_info_paises()
    elif opcao == '2':
        exibir_info_brasil()
    elif opcao == '3':
        exibir_info_empresas()
    elif opcao == '4':
        calcular_porcentagem()
    elif opcao == '5':
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
