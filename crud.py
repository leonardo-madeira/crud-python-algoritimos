def voltar_menu():
    print("Voltar para o menu principal? (s/n)")
    voltar = input().lower()
    if voltar == 's':
        return True
    else:
        return False

def cadastrar_atualizar_cliente():

    print("Cadastro de Cliente")
    print("---------------------")
    print("Preencha os dados a seguir:")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone celular (ex: \"43984117891\"): ")
    cpf = input("Digite o CPF: (ex: \"28057183055\") ")
    endereco = input("Digite o endereço: ")

    if cpf.isdigit() and len(cpf) == 11 and telefone.isdigit() and len(telefone) == 11:
        if "@" in email and "." in email:
            cliente_atual = [nome, email, telefone, cpf, endereco]
            return cliente_atual
    return 0

def listar_clientes(banco_de_dados):
    for index, cliente in enumerate(banco_de_dados):
        print("---------------------")
        print(f"Cliente {index + 1}:")
        print(f"Nome: {cliente[0]}")
        print(f"Email: {cliente[1]}")
        telefone = '({}) {}-{}'.format(cliente[2][:2], cliente[2][2:7],cliente[2][7:11])
        print(f"Telefone: {telefone}")
        cpf = '{}.{}.{}-{}'.format(cliente[3][:3], cliente[3][3:6], cliente[3][6:9], cliente[3][9:])
        print(f"CPF: {cpf}")
        print(f"Endereço: {cliente[4]}")
        print("---------------------")

if __name__ == "__main__":
    banco_de_dados = []

    while True:

        print("Bem-vindo ao sistema de cadastro de clientes!")
        print("Escolha uma opção:")
        print("1. Cadastrar cliente")
        print("2. Listar clientes") 
        print("3. Atualizar cliente")
        print("4. Deletar cliente")
        print("5. Sair")
        opcao = input("Digite sua opção: ")


        if opcao == "1":
            dado = cadastrar_atualizar_cliente()
            if dado:
                banco_de_dados.append(dado)
                print("Cliente cadastrado com sucesso!")
            else:
                print("Erro ao cadastrar cliente. Verifique os dados e tente novamente.")

            voltar = voltar_menu()
            if voltar: continue 
            else: exit()
    
        elif opcao == "2":
            if banco_de_dados:
                listar_clientes(banco_de_dados)       
            else:
                print("Nenhum cliente cadastrado.")
                
            voltar = voltar_menu()
            if voltar: continue 
            else: exit()

        elif opcao == "3":
            cpf_cliente = input("Digite o cpf do cliente que será alterado: ")
            encontrado = False
            for i,pessoa in enumerate(banco_de_dados):
                if pessoa[3] == cpf_cliente:
                    encontrado = True
                    print("Cliente encontrado.")
                    dado_atualizado = cadastrar_atualizar_cliente()
                    if dado_atualizado:
                        banco_de_dados.pop(i)
                        banco_de_dados.append(dado_atualizado)
                        print("Cliente atualizado com sucesso!")
                        voltar = voltar_menu()
                        if voltar: continue 
                        else: exit()
                    else:
                        print("Erro ao atualizar cliente. Verifique os dados e tente novamente.")
                        voltar = voltar_menu()
                        if voltar: continue 
                        else: exit()  
        
            if not encontrado:
                    print("Cliente não encontrado.")
                    voltar = voltar_menu()
                    if voltar: continue 
                    else: exit()  

        elif opcao == "4":
            cpf_cliente = input("Digite o cpf do cliente que será deletado: ")
            for i,pessoa in enumerate(banco_de_dados):
                if pessoa[3] == cpf_cliente:
                    encontrado = True
                    print("Cliente encontrado.")
                    print(f"Você tem certeza que deseja deletar o cliente {pessoa[0]}? (s/n)")
                    confirmacao = input().lower()
                    if confirmacao == 's':
                        banco_de_dados.pop(i)
                        print("Cliente deletado com sucesso!")
                    else:
                        print("Operação cancelada.")
                    
                    voltar = voltar_menu()
                    if voltar: continue 
                    else: exit()  

            if not encontrado:
                print("Cliente não encontrado.")
                voltar = voltar_menu()
                if voltar: continue 
                else: exit()

        elif opcao == "5":
            print("Saindo do sistema...")
            exit()

        else:
            print("Opção inválida. Tente novamente.")
            voltar = voltar_menu()
            if voltar: continue 
            else: exit()
