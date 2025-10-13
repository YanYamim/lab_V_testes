from ex3_salario import Funcionario, CalculadoraDeSalario

def test_desenvolvedor_salario_maior_ou_igual_3000():
    f = Funcionario("João", "joao@email.com", 3000, "DESENVOLVEDOR")
    calc = CalculadoraDeSalario()
    assert calc.calcular_salario_liquido(f) == 2400.00

def test_desenvolvedor_salario_menor_3000():
    f = Funcionario("Maria", "maria@email.com", 2500, "DESENVOLVEDOR")
    calc = CalculadoraDeSalario()
    assert calc.calcular_salario_liquido(f) == 2250.00

def test_dba_salario_maior_ou_igual_2000():
    f = Funcionario("Carlos", "carlos@email.com", 2000, "DBA")
    calc = CalculadoraDeSalario()
    assert calc.calcular_salario_liquido(f) == 1500.00

def test_dba_salario_menor_2000():
    f = Funcionario("Ana", "ana@email.com", 1500, "DBA")
    calc = CalculadoraDeSalario()
    assert calc.calcular_salario_liquido(f) == 1275.00

def test_testador_salario_maior_ou_igual_2000():
    f = Funcionario("Pedro", "pedro@email.com", 2500, "TESTADOR")
    calc = CalculadoraDeSalario()
    assert calc.calcular_salario_liquido(f) == 1875.00

def test_testador_salario_menor_2000():
    f = Funcionario("Julia", "julia@email.com", 1500, "TESTADOR")
    calc = CalculadoraDeSalario()
    assert calc.calcular_salario_liquido(f) == 1275.00

def test_gerente_salario_maior_ou_igual_5000():
    f = Funcionario("Rita", "rita@email.com", 5000, "GERENTE")
    calc = CalculadoraDeSalario()
    assert calc.calcular_salario_liquido(f) == 3500.00

def test_gerente_salario_menor_5000():
    f = Funcionario("Lucas", "lucas@email.com", 4000, "GERENTE")
    calc = CalculadoraDeSalario()
    assert calc.calcular_salario_liquido(f) == 3200.00
