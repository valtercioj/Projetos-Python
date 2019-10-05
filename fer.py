import os
import sys
import subprocess as s
from googlesearch import search
class ClienteNormal(object):
    
#Cliente comum
    
    def __init__(self, name, cpf, e_mail, assinante):
        self.name = name
        self.cpf = cpf
        self.e_mails = ["não Existente", "não Existente"]
        self.assinante = assinante
        if e_mail:
            self.e_mails.remove("não Existente")    
            self.e_mails.append(e_mail)
            

    def dadosClienteNormal(self):
        print('Dados Cliente: \n Name: {0} \n Cpf: {1} \nE-mails: \n E-mail 1 {2} \n E-mail 2 {3} \nSituação: {4}' .format(self.name,self.cpf,self.e_mails[0],self.e_mails[1], self.assinante))

    def adicionarE_mail(self, e_mail):
        print('Adicionando O E-mail: {}'.format(e_mail))
        self.e_mails.remove("não Existente")
        self.e_mails.append("lucebin@gmail.com")

    def mostrarEmails(self):
        print('E_mails Disponiveis {}'.format(self.e_mails))


cliente = ClienteNormal('Lucas Cebin Bortolozi',45740923867,'lucebin@gmail.com','assinante')
print(cliente.dadosClienteNormal())
print(cliente.adicionarE_mail('lucebin@gmail.com'))
print(cliente.dadosClienteNormal())
print(cliente.mostrarEmails())
#Cliente VIP
class ClienteVIP(ClienteNormal):
    def __init__(self, name, cpf, e_mail, assinante, pontos):
        super().__init__(name, cpf, e_mail, assinante)
        self.pontos = pontos

    def adicionaPontosFidelidade(self, pontos):
        print('Creditando pontos de fidelidade em sua conta\n Você tinha {} pontos de fidelidade'.format(self.pontos))
        self.pontos += pontos
        print('Agora você tem {} de fidelidade'.format(self.pontos))

def site():
    os = sys.platform()
    for url in search(opcao+'google', stop=1):
        if os == 'win32':
            os.startfile(url)
        elif os == 'linux':
            s.Popen(['xdg-open'+url])
fulano = ClienteVIP('Aleatorio', 40456398217,'aleatorio@hotmail.com','assinante',56)
print(fulano.dadosClienteNormal())
print(fulano.adicionaPontosFidelidade(15))
