def coletar_informacoes_cliente():
    nome = input("Nome completo do cliente: ")

    while True:
        try:
            idade = int(input("Idade do cliente (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

    print("\nInformações do cliente:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")

coletar_informacoes_cliente()
