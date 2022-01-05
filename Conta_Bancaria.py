class ContaBancaria():
    def __init__(self, saldo, titular):
        self.saldo = float(saldo)
        self.titular = titular     

    def __str__(self):
        return f'{self.titular} --> {self.saldo}'

    def depositar(self, money):
        self.saldo += money 

    def sacar(self, money):
        self.saldo -= money 

class Itau(ContaBancaria):
    def transferencia(self, valor, destino):
        total = (valor + (valor * 0.01))
        if not isinstance(destino, Bradesco):
            print("Transição inválida! Tente novamente...")
        elif destino.titular == self.titular:
            print("Transição inválida")
        elif total > self.saldo:
            print("Saldo insuficiente!")    
        else:
            self.sacar(total)
            destino.depositar(valor)
            print("Transferência realizada com sucesso!")

class Bradesco(ContaBancaria):
        def transferencia(self, valor, destino):
            total = (valor + (valor * 0.005)+5)
            if not isinstance(destino, Itau):
                print("Transição inválida! Tente novamente...")
            elif destino.titular == self.titular:
                print("Transição inválida")
            elif total > self.saldo:
                print("Saldo insuficiente!")    
            else:
                self.sacar(total)
                destino.depositar(valor)
                print("Transferência realizada com sucesso!")
 

class Conta_teste(ContaBancaria):
    def transferir(self, valor, destino):
        self.sacar(valor + ((valor * 0.20)/100) + 10)
        destino.depositar(valor)


conta_1 = Itau(3500, "Patricia")
conta_2 = Bradesco(3000,"Pedro")
conta_bancaria = Conta_teste(5400, "Julio Cesar")

conta_1.transferencia(500, conta_2)
print(conta_1)

conta_2.transferencia(300, conta_1)
print(conta_2)

conta_1.transferencia(400, conta_bancaria)
print(conta_1)


