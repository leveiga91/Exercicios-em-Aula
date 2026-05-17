cliente = input("Bem vindo à Lanchonete Senai! Qual é o seu nome? ")
print(f"Olá, {cliente}! É um prazer atender você.")

print("---- NOSSO CARDÁPIO ----")
print("1. Hamburguer: R$ 25,00")
print("2. Refrigerante: R$ 8,00")
print("-------------------------")

print("\nFaça o seu pedido: ")
qtd_hamburguer = int(input("Quantos Hamburgueres você deseja? "))
qtd_refri = int(input("Quantos Refrigeantes você deseja? "))

print("Seu pedido:")
print(f"Serão {qtd_hamburguer} de Hamburgueres e {qtd_refri} de Refrigerantes")

total_hamburguer = qtd_hamburguer * 25.00
total_refri = qtd_refri * 8.00
valor_total = total_hamburguer + total_refri

print(f"O valor total do seu pedido é R${valor_total}")