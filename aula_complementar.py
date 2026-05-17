print("Seja bem vindo ao Mercado Senai\n" \
"Qual seria seu pedido hoje?\n" \
"1. Realizar compra\n" \
"2. Sair")
pedido1 = int(input("Digite uma opção: "))
if pedido1 == 1:
    print("Você digitou a opção:", pedido1)
    print("PRODUTOS DISPONIVEIS:\n" \
    "1. Arroz 1kg: R$3,99\n" \
    "2. Feijão 1kg: R$6,99\n" \
    "3. Carne 1kg: R$19,99\n" \
    "4. Hortaliças: R$2,99\n" \
    "5. Refrigerante: R$8,99")
    item1 = input("Digite o numero do produto:")
    print("Voce digitou a opção:", item1)
else:
    print("Obrigada pelo contato.\n" \
    "Até a proxima!")