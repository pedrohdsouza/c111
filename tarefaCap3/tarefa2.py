loja1 = {"Iphone 14", "Moto G6", "Samsung S21", "Nokia 3310"}
loja2 = {"Samsung Flip 4", "Zenfone", "Samsung S22", "Nokia 3310"}

print("Loja 1 tem em estoque:" + str(loja1))
print("Loja 2 tem em estoque:" + str(loja2))
print()
print("Você tem as seguintes opções de compra:" + str(loja1.union(loja2)))
print()
print("Modelo que as duas lojas possuem:" + str(loja1.intersection(loja2)))