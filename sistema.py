import json

# 1. Usuários fixos pré-definidos
usuario_1 = {
    "nome": input("digite o seu nome: "),
    "idade": input("digite sua idade: "),
    "linguagem": "Python",
    "versao": 3.11,
    "criador": "Igor Melo"
}

usuario_2 = {
    "nome": "Igor Melo",
    "idade": 17,
    "linguagem": "Python",
    "versao": 3.11,
    "criador": "Igor Melo"
}

# 2. Recolha interativa do terceiro usuário
print("--- Cadastro do Usuário 3 ---")
usuario_3 = {
    "nome": input("Digite o seu nome: "),
    "idade": int(input("Digite a sua idade: ")),
    "linguagem": input("Digite a sua linguagem favorita: "),
    "versao": 3.11,
    "criador": "Igor Melo"
}

# 3. Agrupa todos os usuários em uma única lista
dados_Sistema = [usuario_1, usuario_2, usuario_3]

# 4. Bloco para ESCREVER/SALVAR todos os dados no arquivo JSON
with open("main.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_Sistema, arquivo, indent=4, ensure_ascii=False)

print("\nTodos os dados de todos os usuários foram salvos com sucesso!")

# 5. Bloco separado para LER e VERIFICAR o arquivo gravado
with open("main.json", "r", encoding="utf-8") as arquivo:
    dados_carregados = json.load(arquivo)

# 6. Exibe os dados verificados de forma organizada no terminal
print("\n--- DADOS LIDOS DE DENTRO DO ARQUIVO (JSON) ---")
for i, usuario in enumerate(dados_carregados, start=1):
    print(f"Usuário {i}: Nome: {usuario['nome']} | Idade: {usuario['idade']} | Linguagem: {usuario['linguagem']}")