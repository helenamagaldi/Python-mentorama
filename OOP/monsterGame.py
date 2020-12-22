import datetime as dt



class TipoMonstro():

    def __init__(self, nome, tipo, ps):

        self.nome = nome

        self.tipo = tipo

        self.ps = ps

        self.evolucao = 1

        self.ativo = True

        self.alimentos = 0

        self.data_cap = dt.datetime.today()



    def __str__(self):


        s = ''

        s += 'Nome        :%s\n' % self.nome

        s += 'Tipo        :%s\n' % self.tipo

        s += 'Ponto Saude :%d\n' % self.ps

        s += 'Evolucao    :%d\n' % self.evolucao

        s += 'Ativo       :%s\n' % self.ativo

        s += 'Alimentos   :%d\n' % self.alimentos

        s += 'Data Captura:%s\n' % self.dc

        self.data_cap.strftime('%d/%m/%Y')

        return s



    def reviver(self):

        self.ativo = True



    def desmaiar(self):

        self.ativo = False



    def evoluir(self):

        self.evolucao += 1



    def alimentar(self):

        self.alimentos = 1



class TipoFogo(TipoMonstro):

    def __init__(self, nome, tipo, ps, temperatura, confortavel):
        super().__init__(nome, tipo, ps)

        self.temperatura = temperatura

        self.confortavel = confortavel

    def __str__(self): 

        s = ''

        s += super().__str__()

        s += 'Temperatura    :%d\n' % self.temperatura

        s += 'Confortavel    :%d\n' % self.confortavel

        return s

    def aumentar_Temperatura(self):

        self.temperatura += 1
        print("Eba, está ficando quente!")

    def incendio(self):

        print(self.nome)
        print("Incêndio!")

    def esta_confortavel(self):

        self.ativo = True
        print("Estou feliz!")

    def triste(self):

        self.ativo = False
        print("Tô tisti ):")

monstrinhoFoguento = TipoFogo("Foguinho", "Fogo", 5, 102, True)

class TipoAgua(TipoMonstro):

    def __init__(self, nome, tipo, ps, fluxo, chateado, molhado):
        super().__init__(nome,tipo,ps)

        self.fluxo = fluxo

        self.chateado = chateado

        self.molhado = molhado

    def __str__(self):

        s = ''

        s += super().__str__()

        s += 'fluxo    :%d\n' % self.fluxo

        s += 'Ativo       :%s\n' % self.ativo

        s += 'chateado    :%d\n' % self.chateado

        s += 'molhado    :%d\n' % self.molhado

        return s

    def aumentar_fluxo(self):

        self.fluxo += 1
        print("Chuva forte!")


    def chuva(self):

       print(self.nome)
       print("Chuva!")

    def tipo_chuva(self):

        print(self.nome)
        print("CHUVA!")

    def sem_chuva(self):

        self.ativo = False 
        print("Preciso de mais água!")

    def chateado(self):

        self.ativo = False
        print("Preciso de mais água ):")

    def feliz(self):

        self.ativo = True
        print("Eba, chuva!")

    def cheio_de_agua(self):

        self.ativo = True
        print("Estou bem feliz!")

    def seco(self):

        self.ativo = False
        print("Tá difícil de ficar sem água, por favor me molhe")

monstrinhoMolhado = TipoAgua("Molhado", "Água", 7, 4, False, True)
    
# # não sei pq aqui está aparecendo o monstrinhoMolhado com underline, no VSCode está rodando sem problemas
