class Funcionario:
    def __init__(self, nome: str, email: str, salario_base: float, cargo: str):
        self.nome = nome
        self.email = email
        self.salario_base = salario_base
        self.cargo = cargo.upper()  


class CalculadoraDeSalario:
    def calcular_salario_liquido(self, funcionario: Funcionario) -> float:
        salario = funcionario.salario_base
        cargo = funcionario.cargo

        if cargo == "DESENVOLVEDOR":
            return self._calcular_desenvolvedor(salario)
        elif cargo in ["DBA", "TESTADOR"]:
            return self._calcular_dba_ou_testador(salario)
        elif cargo == "GERENTE":
            return self._calcular_gerente(salario)
        else:
            raise ValueError(f"Cargo inválido: {cargo}")

    def _calcular_desenvolvedor(self, salario):
        if salario >= 3000:
            return salario * 0.8
        return salario * 0.9

    def _calcular_dba_ou_testador(self, salario):
        if salario >= 2000:
            return salario * 0.75
        return salario * 0.85

    def _calcular_gerente(self, salario):
        if salario >= 5000:
            return salario * 0.7
        return salario * 0.8
