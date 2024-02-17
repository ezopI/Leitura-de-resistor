# Função quantidade de faixas de 3 ou 4
def quantidade_faixas():
    while True:
        try:
            quantidade = int(input('Quantas faixas o resistor possui (3 ou 4)? '))
            if quantidade not in (3,4):
                print('Por favor, escolhe entre 3 ou 4.')
            else:
                return quantidade
        except ValueError:
            print('Por favor, insira um número válido.')    

# Função de cores das faixas
def cores_faixas(faixa1, faixa2, faixa3, faixa4=None):
    cores = {
        'preto': 0,
        'marrom': 1,
        'vermelho': 2,
        'laranja': 3,
        'amarelo': 4,
        'verde': 5,
        'azul': 6,
        'violeta': 7,
        'cinza': 8,
        'branco': 9
        }
    multiplicadores = {
        'preto': 1,
        'marrom': 10,
        'vermelho': 100,
        'laranja': 1000,
        'amarelo': 10000,
        'verde': 100000,
        'azul': 1000000,
        'violeta': 10000000,
        'cinza': 100000000,
        'branco': 1000000000
    }
    tolerancia = {
        'marrom': "+/- 1%",
        'vermelho': "+/- 2%",
        'verde': "+/- 0.5%",
        'azul': "+/- 0.25%",
        'violeta': "+/- 0.1%",
        'cinza': "+/- 0.05%",
        'dourado': "+/- 5%",
        'prata': "+/- 10%"
    } 
    valor = (cores[faixa1] * 10 + cores[faixa2]) * multiplicadores[faixa3]

    if faixa4:
        return f'{valor} Ohms, tolerância {tolerancia[faixa4]}'
    else:
        return f'{valor} Ohms' 

# Função de seleção das cores para as faixas
def selecao_cores(numeros):
    cores_disponiveis = {'preto','marrom', 'vermelho', 'laranja',
    'amarelo', 'verde', 'azul', 'violeta', 'cinza', 'branco', 'dourado', 'prata'
}
    print(f'''\x1b[38;5;192m
            PRETO [0]
            MARROM [1]
            VERMELHO [2]
            LARANJA [3]
            AMARELO [4]
            VERDE [5]
            AZUL [6]
            VIOLETA [7]
            BRANCO [8]
            \x1b[m''')
    while True:
        if numeros is 4:
            print('-=-'*27)
            print(f'''      
            \x1b[38;5;193m
            MARROM [+/- 1%]
            VERMELHO [+/- 2%]
            VERDE [+/- 0.5%]
            AZUL [+/- 0.25%]
            VIOLETA [+/- 0.1%]
            CINZA [+/- 0.05%]
            DOURADO [+/- 5%]
            PRATA [+/- 10%]
            \x1b[m''')
        cor = str(input(f'Digite a cor da {numeros}ª faixa: ')).lower()
        if cor in cores_disponiveis:
            return cor
        else:
            print('Cor inválida. Por favor, escolha uma cor válida.')

faixasssss = quantidade_faixas()

faixa1 = selecao_cores(1)
faixa2 = selecao_cores(2)
faixa3 = selecao_cores(3)

if faixasssss == 3:
    print('***'*30)
    print(f'\x1b[38;5;177mVocê escolheu um resistor com as cores {faixa1}, {faixa2} e {faixa3}.')
    print(f'A resistência é {cores_faixas(faixa1, faixa2, faixa3)}\x1b[m')
    print('***'*30)
else:
    faixa4 = selecao_cores(4)
    print('***'*30)
    print(f'\x1b[38;5;177mVocê escolheu um resistor com as cores {faixa1}, {faixa2}, {faixa3} e {faixa4}.')
    print(f'A resistencia é {cores_faixas(faixa1, faixa2, faixa3, faixa4)}\x1b[m')
    print('***'*30)