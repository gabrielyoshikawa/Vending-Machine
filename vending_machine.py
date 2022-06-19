#Criação da matriz dos produtos
tabela = [['id', 'produto', 'valor', 'estoque'], [1, 'Coca-cola', 3.75, 2], [2, 'Pepsi', 3.67, 5], [3, 'Monster', 9.96, 1], [4, 'Café', 1.25, 100], [5, 'Redbull', 13.99, 2]]
for j in tabela:
    print (j)

#Seleciona a bebida
def Troco():
    if user_choice == 1:
        preco = tabela[1][2]

    elif user_choice == 2:
        preco = tabela[2][2]

    elif user_choice == 3:
        preco = tabela[3][2]

    elif user_choice == 4:
        preco = tabela[4][2]

    elif user_choice == 5:
        preco = tabela[5][2]
#Input Cliente
    valor_pago = float(input("Insira a quantidade em reais para pagar o produto: "))
#Confere se o input cliente é maior do que o preço do produto
    if(valor_pago < preco):
        print("Erro - Insira uma quantidade maior do que a do produto")
    elif(valor_pago == preco):
        print("Troco de R$0,00")
#Troco na menor quantidade possível de notas e moedas
    else:
        troco = valor_pago - preco
        print(troco)

        notas_200 = troco // 200
        print("Notas de 200,00 Reais: {0}".format(notas_200))

        troco = troco - (notas_200 * 200)
        notas_100 = troco // 100
        print("Notas de R$100,00: {0}".format(notas_100))

        troco = troco - (notas_100 * 100)
        notas_50 = troco // 50
        print("Notas de R$50,00: {0}".format(notas_50))
        
        troco = troco - (notas_50 * 50)
        notas_20 = troco // 20
        print("Notas de R$20,00: {0}".format(notas_20))

        troco = troco - (notas_20 * 20)
        notas_10 = troco // 10 
        print("Notas de R$10,00: {0}".format(notas_10))

        troco = troco - (notas_10 * 10)
        notas_5 = troco // 5 
        print("Notas de R$5,00: {0}".format(notas_5))

        troco = troco - (notas_5 * 5)
        notas_2 = troco // 2 
        print("Notas de R$2,00: {0}".format(notas_2))

        troco = troco - (notas_2 * 2)
        moedas_1 = troco // 1 
        print("Moedas de R$1,00: {0}".format(moedas_1))

        troco = troco - (moedas_1 * 1)
        moedas_50 = troco // 0.5 
        print("Moedas de R$0.50: {0}".format(moedas_50))

        troco = troco - (moedas_50 * 0.5)
        moedas_25 = troco // 0.25
        print("Moedas de R$0.25: {0}".format(moedas_25))

        troco = troco - (moedas_25 * 0.25)
        moedas_10 = troco // 0.1
        print("Moedas de R$0.10: {0}".format(moedas_10))

        troco = troco - (moedas_10 * 0.10)
        moedas_5 = troco // 0.5 
        print("Moedas de R$0.05: {0}".format(moedas_5))

        troco = troco - (moedas_5 * 0.05)
        moedas_01 = troco // 0.01
        print("Moedas de R$0.01: {0}".format(moedas_01))
    
#Estoque
def Estoque():
    if user_choice == 1:
        if tabela[1][3] == 0:
            print("Sem estoque")
        else:
            print("O produto custa:", tabela[1][2], "Reais")
            tabela[1][3] -= 1
            Troco()
    elif user_choice == 2:
        if tabela[2][3] == 0:
            print("Sem estoque")
        else:
            print("O produto custa:", tabela[2][2], "Reais")
            tabela[2][3] -= 1
            Troco()
    elif user_choice == 3:
        if tabela[3][3] == 0:
            print("Sem estoque")
        else:
            print("O produto custa:", tabela[3][2], "Reais")
            tabela[3][3] -= 1
            Troco()
    elif user_choice == 4:
        if tabela[4][3] == 0:
            print("Sem estoque")
        else:
            print("O produto custa:", tabela[4][2], "Reais")
            tabela[4][3] -= 1
            Troco()
    elif user_choice == 5:
        if tabela[5][3] == 0:
            print("Sem estoque")
        else:
            print("O produto custa:", tabela[5][2], "Reais")
            tabela[5][3] -= 1
            Troco()
    else:
        print("ID não encontrado")


verificacao = True

while verificacao:

    user_choice = int(input("Selecione o id da bebida escolhida: "))
    Estoque()
    escolher_novamente = int(input("Deseja escolher outra bebida? Sim(1) Não(2): "))
    if escolher_novamente == 1:
        verificacao = True
    else:
        verificacao = False
 