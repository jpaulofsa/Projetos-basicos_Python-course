# Calculadora em Python

print("\n******************* Python Calculator *******************\n")
print("Selecione o número da operação desejada:")
print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão\n")

opcao = int(input("Digite sua opção (1/2/3/4): "))
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if opcao == 1:
    print("%s + %s =" %(n1, n2), n1+n2)
elif opcao == 2:
    print("%s - %s =" %(n1, n2), n1-n2)
elif opcao == 3:
    print("%s * %s =" %(n1, n2), n1*n2)
elif opcao == 4:
    # Tratamento de exceção
    try:
        n1 / n2
    except ZeroDivisionError:
        print("\nATENÇÃO: Divisão por zero não permitida!!!")
    else:
        print("%s / %s =" %(n1, n2), n1/n2)
else:
    print("\nOpção Inválida!")
    
