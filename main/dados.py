# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet (como por exemplo códigos gerados por IA).
# Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

# Importação de biblioteca
import json


# Dicionário onde é armazenados os valores das bases e dos complementos
bases = {"leite": 4.35, "maracujá": 4.60, "rosa": 5.85, "manga": 5.47}
complementos = {"boba": 0.50, "lichia": 0.75, "geleia": 0.65, "taro": 1.00, "chia": 0.35}

# cria listas auxiliares recebendo a chave e valores de cada dicionário
lista_bases = list(bases.keys())
itens_b = list(bases.values())
lista_complementos = list(complementos.keys())
itens_c = list(complementos.values())

# Classe que representará um cliente
class Cliente:
    def __init__(self, id, nome, tipo):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.cashback = 0.0

    # Adiciona o cliente ao ficheiro "clientes.txt"
    def criar_cliente(self):
        with open("clientes.txt", "a", encoding="utf-8") as arquivo:
            json.dump({'ID': self.id, 'Nome': self.nome, 'Tipo': self.tipo, 'cashback': self.cashback}, arquivo, ensure_ascii=False)
            arquivo.write("\n")

    # Verifica se o cliente com o ID já existe no ficheiro
    def verificar_id(id_procurado):
        with open("clientes.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                cliente = json.loads(linha)
                if cliente['ID'] == id_procurado:
                    c = Cliente(cliente['ID'], cliente['Nome'], cliente['Tipo'])
                    c.cashback = cliente.get('cashback', 0.0)
                    return c
            return False

    # Atualiza apenas o cashback do cliente em específico
    def atualizar_cliente(self):
        with open("clientes.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        with open("clientes.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas:
                cliente = json.loads(linha)
                if cliente['ID'] == self.id:
                    cliente['cashback'] += self.cashback
                json.dump(cliente, arquivo, ensure_ascii=False)
                arquivo.write("\n")

# Classe que representa um pedido
class Pedido:
    def __init__(self, cliente, base, complemento, autorizar = False):
        self.cliente = cliente
        self.base = base
        self.complemento = complemento
        self.valor_total = 0.0
        self.valor_bruto = 0.0
        self.cashback_utilizado = autorizar

    # Calcula o valor total com descontos e cashback
    def calcular_total(self):
        self.valor_total = itens_b[self.base]
        for c in self.complemento:
            self.valor_total += itens_c[c]

        if self.cliente.tipo == 'E':
            self.valor_total *= 0.75
        elif self.cliente.tipo == 'T':
            self.valor_total -= 1

        # Aplica cashback se autorizado
        if self.cashback_utilizado:
            self.valor_total -= self.cliente.cashback
            self.cliente.cashback = 0.0
            with open("clientes.txt", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()

            with open("clientes.txt", "w", encoding="utf-8") as arquivo:
                for linha in linhas:
                    cliente = json.loads(linha)
                    if cliente['ID'] == self.cliente.id:
                        cliente['cashback'] = 0.0
                    json.dump(cliente, arquivo, ensure_ascii=False)
                    arquivo.write("\n")

        self.valor_bruto = self.valor_total
        self.cliente.cashback += self.valor_bruto * 0.1
        return self.valor_bruto

    # Exibe e grava um resumo do pedido
    def resumo_pedido(self):
        if self.cliente.tipo == 'E':
            formato = 'Estudante'
        elif self.cliente.tipo == 'T':
            formato = 'Professor/Funcionário'
        else:
            formato = 'Comum'
        print("\n===== RESUMO DO PEDIDO =====")
        print(f"ID: {self.cliente.id} (Cliente: {self.cliente.nome})")
        print(f"Tipo do Cliente: {formato}")
        print(f"Base: {lista_bases[self.base]}")

        if self.complemento:
            nomes = []
            for c in self.complemento:
                nomes.append(lista_complementos[c])
            adicionais = ', ' .join(nomes)
            print(f"Adicionais: {adicionais}")
        else:
            print("Adicionais: Nenhum")

        print(f"Valor Total: R$ {self.valor_bruto:.2f}")

        if self.cashback_utilizado:
            cbu = 'Sim'
            print("Cashback: Utilizado")
        else:
            cbu = 'Não'
            print("Cashback: Não utilizado")

        print(f"Saldo de Cashback: R$ {self.cliente.cashback:.2f}")
        print("============================\n")

        # Salva os dados do pedido
        with open("pedidos.txt", "a", encoding="utf-8") as arquivo:
            dados = {'ID': self.cliente.id,
                     'Nome': self.cliente.nome,
                     'Tipo': formato,
                     'Base': lista_bases[self.base],
                     'Adicionais': adicionais,
                     'Valor Total': f'R${self.valor_bruto:.2f}',
                     'Cashback Utilizado': cbu,
                     'Saldo de Cashback Atual': f'R${self.cliente.cashback:.2f}'}
                
            json.dump(dados, arquivo, ensure_ascii=False)
            arquivo.write("\n")
