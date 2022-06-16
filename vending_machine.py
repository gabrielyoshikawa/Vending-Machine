tabela = [['id', 'produto', 'valor', 'estoque'], [1, 'Coca-cola', 3.75, 2], [2, 'Pepsi', 3.67, 5], [3, 'Monster', 9.96, 1], [4, 'Café', 1.25, 100], [5, 'Redbull', 13.99, 2]]
for j in tabela:
    print (j)

notasMoedas = [200,100,50,20,10,5,2,1,0.5,0.25,0.1,0.05]

verification = True
while verification:
        
    def EscolherBebida():
        user_choice = int(input("Selecione o id da bebida escolhida: "))
        if user_choice == 1:
            if tabela[1][3] == 0:
                print("Sem estoque")
            else:
                print("O produto custa:", tabela[1][2], "Reais")
                valorPago = int(input("Insira o valor a ser pago: "))
                if valorPago < tabela[1][2]:
                    print("Não foi possível realizar a compra - Valor insuficiente")
                else:
                    troco = valorPago - tabela[1][2]
                    if valorPago > tabela[1][2]:
                        trocofinal = 0
                        for i in range(len(notasMoedas)):
                            if troco > notasMoedas[i]:
                                trocofinal += notasMoedas[i]
                    print(trocofinal)
                    tabela[1][3] -= 1

        elif user_choice == 2:
            if tabela[2][3] == 0:
                print("Sem estoque")
            else:
                print("O produto custa:", tabela[2][2], "Reais")
                valorPago = int(input("Insira o valor a ser pago: "))
                if valorPago < tabela[2][2]:
                    print("Não foi possível realizar a compra - Valor insuficiente")
                else:
                    print(valorPago - tabela[2][2])
                    tabela[2][3] -= 1

        elif user_choice == 3:
            if tabela[3][3] == 0:
                print("Sem estoque")
            else:
                print("O produto custa:", tabela[3][2], "Reais")
                valorPago = int(input("Insira o valor a ser pago: "))
                if valorPago < tabela[3][2]:
                    print("Não foi possível realizar a compra - Valor insuficiente")
                else:
                    print(valorPago - tabela[3][2])
                    tabela[3][3] -= 1

        elif user_choice == 4:
            if tabela[4][3] == 0:
                print("Sem estoque")
            else:
                print("O produto custa:", tabela[4][2], "Reais")
                valorPago = int(input("Insira o valor a ser pago: "))
                if valorPago < tabela[4][2]:
                    print("Não foi possível realizar a compra - Valor insuficiente")
                else:
                    print(valorPago - tabela[4][2])
                    tabela[4][3] -= 1

        elif user_choice == 5:
            if tabela[5][3] == 0:
                print("Sem estoque")
            else:
                print("O produto custa:", tabela[5][2], "Reais")
                valorPago = int(input("Insira o valor a ser pago: "))
                if valorPago < tabela[5][2]:
                    print("Não foi possível realizar a compra - Valor insuficiente")
                else:
                    print(valorPago - tabela[5][2])
                    tabela[5][3] -= 1

        else:
            print("ID não encontrado")   

    EscolherBebida()

    escolher_novamente = int(input("Deseja escolher outra bebida? Sim(1) Não(2): "))
    if escolher_novamente == 2:
        verification = False
    else:
        verification = True
