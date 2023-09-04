import itertools
import re

def ler_conjunto(conjunto_str):
    elementos = re.findall(r'[A-Za-z0-9]+', conjunto_str)
    return set(elementos)

def realizar_operacao(nome_arquivo):
    if "U" in nome_arquivo:
        operacao = 'uniao'
    elif "I" in nome_arquivo:
        operacao = 'interseccao'
    elif "D" in nome_arquivo:
        operacao = 'diferenca'
    elif "C" in nome_arquivo:
        operacao = 'produto_cartesiano'
    else:
        print('Nome de arquivo inválido')
        return

    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    if operacao != 'produto_cartesiano' and len(linhas) != 2:
        print('Arquivo mal formatado. Deve conter exatamente dois conjuntos para essa operação.')
        return

    if operacao == 'produto_cartesiano' and len(linhas) != 3:
        print('Arquivo mal formatado. Deve conter exatamente três conjuntos para o produto cartesiano.')
        return

    conjunto1 = ler_conjunto(linhas[0])
    conjunto2 = ler_conjunto(linhas[1])
    
    resultado = None

    if operacao == 'uniao':
        resultado = conjunto1.union(conjunto2)
    elif operacao == 'interseccao':
        resultado = conjunto1.intersection(conjunto2)
    elif operacao == 'diferenca':
        resultado = conjunto1.difference(conjunto2)
    elif operacao == 'produto_cartesiano':
        conjunto3 = ler_conjunto(linhas[2])
        resultado = list(itertools.product(conjunto1, conjunto2, conjunto3))
    else:
        print('Operação inválida')
        return

    if operacao == 'produto_cartesiano':
      print(conjunto1)
      print(conjunto2)
      print(conjunto3)
      print(resultado)

    else:
      print(conjunto1)
      print(conjunto2)
      print(resultado)

# Substitua 'C.txt' pelo nome do arquivo que você deseja usar
realizar_operacao('D.txt')