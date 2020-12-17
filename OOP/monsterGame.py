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

        pass



    def evoluir(self):

        self.evolucao += 1



    def alimentar(self):

        self.alimentos = True

        pass



class TipoFogo(TipoMonstro):

    def __init__(self, nome, tipo, ps, temperatura):

        # fazer

        pass