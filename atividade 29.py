# Solicita ao usuário que insira os nomes dos alunos presentes
alunos_presentes = input("Alunos presentes (separe os nomes por vírgula): ").split(',')

# Remove espaços em branco dos nomes
alunos_presentes = [aluno.strip() for aluno in alunos_presentes]

# Conta o número de alunos presentes
numero_alunos = len(alunos_presentes)

# Exibe a quantidade de alunos e a lista de nomes
print(f"Alunos presentes: {numero_alunos}")
print("Lista de alunos presentes:", ', '.join(alunos_presentes))

# Verifica se o número de alunos é menor que 5
if numero_alunos < 5:
    print("Aviso: Poucos alunos presentes. Revisar lista de chamada.")