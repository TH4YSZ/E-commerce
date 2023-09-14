class Cliente:
    def __init__(self, id, nome, cpf, tel, senha):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.tel = tel
        self.senha = senha

class Produto:
    def __init__(self, num, nomePd, precoPd, qtd):
        self.num = num
        self.nomePd = nomePd
        self.precoPd = precoPd
        self.qtd = qtd


class E_commerce:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.clientes = {}
        self.produtos = {}
        self.carrinhos = {}

    def cadastrar_cliente(self, id, nome, cpf, tel, senha):
        cliente = Cliente(id, nome, cpf, tel, senha)
        self.clientes[id] = cliente

    def login(self, cpf, senha):
        for id, cliente in self.clientes.items():
            if cpf == cliente.cpf and senha == cliente.senha:
                return id
        return None

    def cadastrar_produto(self, num, nomePd, precoPd, qtd):
        produto = Produto(num, nomePd, precoPd, qtd)
        self.produtos[num] = produto

    def listar_produtos(self):
        for num, produto in self.produtos.items():
            print(f"{num} - Nome: {produto.nomePd}, Valor: R${produto.precoPd}, Quantidade: {produto.qtd}")

    def adicionar_carrinho(self, cliente_id, produto_id, qtdp):
        carrinho = Carrinho(cliente_id, produto_id, qtdp)
        self.carrinho[id] = carrinho
        