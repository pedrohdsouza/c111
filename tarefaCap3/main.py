# Coleções - Tipo de dado que está devidamente estruturado para receber mais de um valor (variável composta)
# 1 - TUPLA (Tuples)

# UMA COLEÇÃO IMUTAVEL, NÃO PODE ADICIONAR, DELETAR, NEM ALTERAR ELEMENTOS DE UMA TUPLA

#nomes = ("Goku", "Vegeta", "Trunks", "Gohan")x

#print(nomes)

# nomes[0] = "Piccolo" Tupla não permite mexer nos elementos

#print(nomes[0])


# 2 - LISTA (Lists)

# UMA COLEÇÃO MUTÁVEL

#nomes = ["Goku", "Vegeta", "Trunks", "Gohan"]
#print(type(nomes)) retorna o tipo da variável

#print(nomes)

# INSERT
#nomes.append('Pan')
#print(nomes)

# UPDATE
#nomes[0] = 'Piccolo'
#print(nomes)

# DELETE
# REMOCAO POR VALOR
#nomes.remove("Trunks")
#print(nomes)

# REMOCAO POR INDICE
#nomes.pop(2)
#print(nomes)

# 3 - CONJUNTO (Set)
# NAO GUARDA ELEMENTOS REPETIDOS
# NAO GUARDA INDICES
#nomes = {"Goku", "Goku", "Vegeta", "Trunks", "Gohan"}
#nomes.add("Kuririn")
#nomes.remove("Trunks")
#print(nomes)

# 4 - DICIONARIO (Dictionary)
# índices Customizados

pessoa = {
            "nome": "Goku", 
            "idade": 42
         }

# ADD
pessoa["sexo"] = "M"

# UPDATE
pessoa["idade"] = 40

# DELETE
del pessoa["nome"]

print(pessoa)


