# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet (como por exemplo códigos gerados por IA).
# Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

# Importação de bibliotecas
import json
import dados


comple = [] # Lista para armazenar temporariamente os complementos escolhidos
autorizar = False # Indica se o cliente irá usar o cashback

# Cria o ficheiro de clientes caso ainda não exista
arquivo = open("clientes.txt", "a")
arquivo.close()

# Loop principal do menu
menu = True
while menu:
    escolha = input("--- MENU PRINCIPAL ---\n"
                    "< 1 > Novo pedido\n"
                    "< 2 > Mostrar pedidos\n"
                    "< 3 > Sair\n"
                    "< = > ")

    # Criar novo pedido
    if escolha == '1':
        a = True
        while a:
            id = input("ID do Cliente (4 Dígitos): ")
            if len(id) == 4 and id.isnumeric(): # Verifica se ID é válido
                cliente_existente = dados.Cliente.verificar_id(id)
                if cliente_existente:
                    print("ID já existente! Usando dados do cliente existente.")
                    cliente_atual = cliente_existente
                    a = False
                else:
                    nome = input("Nome do Usuário: ")
                    b = True
                    while b:
                        tipo = input("Estudante(E) | Professor/Funcionário(T) | Comum(C)\n"
                                     "< = > ").upper()
                        if tipo in ['E', 'T', 'C']:
                            cliente_atual = dados.Cliente(id, nome, tipo)
                            cliente_atual.criar_cliente()
                            b = False
                        else:
                            print("Tipo inválido!")
                    a = False
            else:
                print("ID inválido. Apenas 4 dígitos numéricos!")

        # Escolha da base
        c = True
        while c:
            try:
                base = int(input("=== Escolha uma base ===\n"
                                "< 1 > Leite: R$ 4,35\n"
                                "< 2 > Maracujá: R$ 4,60\n"
                                "< 3 > Rosa: R$ 5,85\n"
                                "< 4 > Manga: R$ 5,47\n"
                                "< = > "))
                if base in [1, 2, 3, 4]:
                    base -= 1
                    c = False
                else:
                    print("Opção invalida!")
            except:
                print("Opção inválida!")

        # Escolha do complemento
        d = True
        while d:
            try:
                complemento = int(input("=== Complementos ===\n"
                                        "< 1 > boba: R$ 0,50\n"
                                        "< 2 > lichia: R$ 0,75\n"
                                        "< 3 > geleia: R$ 0,65\n"
                                        "< 4 > taro: R$ 1,00\n"
                                        "< 5 > chia: R$ 0,35\n"
                                        "< 6 > Parar\n"
                                        "< = > "))
                if complemento in [1, 2, 3, 4, 5]:
                    comple.append(complemento - 1) # Guarda os complementos
                elif complemento == 6:
                    d = False
                else:
                    print("Opção invalida!")
            except:
                print("Opção inválida!")

        # Verifica e pergunta sobre o uso do cashback
        if cliente_atual.cashback > 0:
            e = True
            while e:
                cb = input(f"Você tem R${cliente_atual.cashback:.2f} de cashback.\n"
                           "Deseja utilizar? (S/N) => ").upper()
                if cb == 'S':
                    autorizar = True
                    print("Cashback utilizado!")
                    e = False
                elif cb == 'N':
                    e = False
                else:
                    print("Opção inválida!")

        # Cria e processa o pedido
        pedido_atual = dados.Pedido(cliente_atual, base, comple, autorizar)
        pedido_atual.calcular_total()
        pedido_atual.resumo_pedido()
        cliente_atual.atualizar_cliente()
        comple.clear()

    # Mostrar pedido
    elif escolha == '2':
        f = True
        while f:
            try:
                print("===== Mostrar Pedidos =====")
                mostrar = int(input("< 1 > Mostrar pedido específico\n"
                                    "< 2 > Mostrar todos os pedidos\n"
                                    "< 3 > Voltar para o menu\n"
                                    "< = > "))
                if mostrar == 1:
                    id = input("ID do Cliente desejado: ")
                    if dados.Cliente.verificar_id(id):
                        with open("pedidos.txt", "r", encoding="utf-8") as arquivo:
                            print("=-" * 30)
                            for pedido in arquivo:
                                cliente = json.loads(pedido)
                                if cliente['ID'] == id:
                                    for c, v in cliente.items():
                                        print(f"{c}: {v}")
                                    print("=-" * 30)
                    else:
                        print("Usuário não encontrado!")
                elif mostrar == 2:
                        with open("pedidos.txt", "r", encoding="utf-8") as arquivo:
                            print("=-" * 30)
                            for dic in arquivo:
                                cliente = json.loads(dic)
                                for c, v in cliente.items():
                                    print(f"{c}: {v}")
                                print("=-" * 30)
                elif mostrar == 3:
                    print("Voltando ao menu...")
                    f = False
                else:
                    print("Opção inválida")
            except:
                print("Opção inválida!")

    # Finalizar o programa
    elif escolha == '3':
        print("FECHANDO O PROGRAMA...")
        menu = False

    else:
        print("Opção inválida")
