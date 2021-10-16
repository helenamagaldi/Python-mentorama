

class GeraFibo:
    qtde = int(input("QUANTOS TREM VC QUER"))

    def __iter__(self):
        self.var = self.qtde - 2
        self.a1 = 0
        self.a2 = 1
        self.lista = [self.a1, self.a2]

        return self

    def __next__(self):
        proximo = self.a1 + self.a2
        self.lista.append(proximo)
        self.var -= 1
        self.a1 = self.a2
        self.a2 = proximo

        if self.var == 0:
            fibo2 = {k+1 : v for k, v in enumerate(self.lista)}
            print(fibo2)
            raise StopIteration

        return self.lista

cont = GeraFibo()
gerar_numeros = iter(cont)
next(cont)