#Nome: Henrique Xavier Ribeiro
#RA: 20170180

class ClienteComum(object):
    def __init__(self, nome, cpf, email1, email2, situacao, quantidadeClientes):
        self.nome = nome
        self.cpf = cpf
        self.email1 = email1
        self.email2 = email2
        self.situacao = situacao
        self.quantidadeClientes = quantidadeClientes

    def descricao(self):
        print('Nome: {}\nCPF: {}\nEmail1: {}\nEmail2: {}\nSituação: {}\nClientes: {}'.format(self.nome,self.cpf,self.email1,self.email2,self.situacao,self.quantidadeClientes))

Hulk = ClienteComum('Hulk Rossum', 402887201, 'hulk@avengers.org', 'cede@avengers.org', 'Operante', 12)
print(Hulk.descricao())


class ClienteVip(ClienteComum):
    def __init__(self, nome, cpf, email1, email2, situacao,quantidadeClientes, numeroFidelidade, pontosFidelidade, endereco):
        super().__init__(nome, cpf, email1, email2, situacao,quantidadeClientes)
        self.numeroFidelidade = numeroFidelidade
        self.totalPontos = pontosFidelidade
        self.endereco = endereco

    def dadosVip(self,totalPontos):
        print('Seus pontos são {}'.format(self.totalPontos,self.nome))


Thanos = ClienteVip('Raul',1234567,'raul@raul','raul2@raul2','cadastrado',2,764,12,'rua do amor')
print(Thanos.dadosVip(32))