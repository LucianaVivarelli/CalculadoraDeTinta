# criando um programa que calcula a quantidade de tinta necessária para pintar uma parede.

# O usuario deverá fornecer as informações de rendimento, altura e largura.

# Isso tornará uma resposta com a mensagem ' você necessita de x latas de tinta'


rendimento = float(input('Qual é o rendimento da lata?'))
altura = float(input('Qual é a alura da lata?'))
largura = float(input('Qual é a largura da lata?'))

def calculo_tinta():
    area = altura * largura
    total = area / rendimento
    print(f'Você precisa de {total} latas de tinta')

calculo_tinta()    