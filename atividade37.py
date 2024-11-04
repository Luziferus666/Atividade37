#Ler um vetor com 20 idades e exibir a maior e menor.
idades = [int(input(f"Digite a idade {i + 1}: ")) for i in range(20)]
maior_idade = max(idades)
menor_idade = min(idades)
print("Maior idade:", maior_idade)
print("Menor idade:", menor_idade)