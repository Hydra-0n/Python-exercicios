def lernotas():
    n=float(input("Digite o valor das notas: "))
    return n

def resultado(n1,n2):
    media = (n1+n2)/2
    print("valor da N1:", n1)
    print("valor da N2:", n2)
    print("Media:", media, "Resultado:", end="")
    if (media >= 7):
        print("Aprovado")
    else:
        print("Reprovado")

a = lernotas()
b = lernotas()
resultado (a,b)

