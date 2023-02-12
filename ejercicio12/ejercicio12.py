class Cuenta:
    def __init__(self, numero_cuenta, balance, limite_sobregiro=0):
        self.numero_cuenta = numero_cuenta
        self.balance = balance
        self.limite_sobregiro = limite_sobregiro

    def deposito(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        if self.balance - cantidad >= -self.limite_sobregiro:
            self.balance -= cantidad
            return True
        else:
            return False

    def obtener_balance(self):
        return self.balance
