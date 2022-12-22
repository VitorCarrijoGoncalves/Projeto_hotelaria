


# print([x + 10 for x in range (5)])


# list(range(0,10,2))


# print({n for n in range(11) if n % 2 == 1})


# pessoas = [' Ana ', 'manuela', 'FELIPe', 'Pedr0 ']

# ana = '  Ana  '

# print(ana.strip().capitalize())


# pessoas_normalizadas = [pessoas.strip().capitalize() for pessoa in pessoas]

# print(pessoas_normalizadas)


meu_dicionario = [{'nome': 'Ana', 'idade': 80},
                  {'nome': 'Jose', 'idade': 45},
                  {'nome': 'Maria', 'idade': 10}]


# print(meu_dicionario[2]['nome'])


loteria = {'nome': 'Fulano', 'numero': (13,4,53,67,82)}



# print(loteria)




universidades = [
    {
        'nome': 'Universidade de São Paulo',
        'sigla': 'USP'
    },
    {
        'nome': 'Universidade do Rio de Janeiro',
        'sigla': 'UFRJ'
    }
]



# print(sum(loteria['numero']))

loteria['nome'] = 'Ana'



jogador_loteria_1 = {
    'nome': 'Pedro',
    'numeros': (13,4,52,23,67,82)
}

jogador_loteria_2 = {
    'nome': 'Pedro',
    'numeros': (13,4,52,23,67,82)
}



class JogadorLoteria:
    def __init__(self):
        self.nome = 'Pedro'
        self.numeros = (13,4,52,23,67,82)

    def total(self):
        return sum(self.numeros)

jogador_1 = JogadorLoteria()
jogador_2 = JogadorLoteria()

jogador_1.nome

jogador_1.numeros


jogador_1.total()










class Funcionario():

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return {'nome': self.nome, 'salário': self.salario}


fabio = Funcionario('Fabio', 7000)

print(fabio.dados())




class Admin(Funcionario):

    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def atualizar_dados(self, nome):
        self.nome = nome
        return self.dados()


fernando = Admin('Fernando', 14000)
