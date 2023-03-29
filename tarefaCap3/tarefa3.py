nome = (str(input("Entre com nome do aluno:")))
media = (float(input("Entre com a média:")))

aluno = {"Nome": nome, "Media": media}

if (media >= 60):
    aluno["Situação"] = "AP"
else:
    aluno["Situação"] = "RP"

print(aluno)