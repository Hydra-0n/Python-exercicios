qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while valor < 10:
    soma = soma + valor
    qtd = qtd + 1
    valor = float(input("Digite um valor: "))

media = soma / qtd
print("\n total da soma", soma)
print("\n total dos valores digitados", qtd)
print("\n media dos valores digitados", media)