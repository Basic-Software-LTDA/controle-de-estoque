print ("Controle de estoque")
print (". . . . .")
def estoque():
    cont = "S"
    est = 0
    while cont == "S":
        prod = input("Digite o produto: ")
        qtde = int(input("Digite a quantidade: "))
        cont = input("Continuar? S/N: ")
        est = est + qtde
    return est

estoq = str(estoque())

print (". . . ")
print (f"O total de produtos em estoque é: " + estoq)
print (" Fim do programa")