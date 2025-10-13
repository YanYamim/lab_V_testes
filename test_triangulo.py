from ex1_triangulo import Triangulo

# Triângulos válidos

def test_escaleno_valido():
    assert Triangulo(3, 4, 5).tipo() == "Escaleno"

def test_isosceles_valido_1():
    assert Triangulo(5, 5, 3).tipo() == "Isósceles"

def test_isosceles_valido_2():
    assert Triangulo(5, 3, 5).tipo() == "Isósceles"

def test_isosceles_valido_3():
    assert Triangulo(3, 5, 5).tipo() == "Isósceles"

def test_equilatero_valido():
    assert Triangulo(4, 4, 4).tipo() == "Equilátero"

# Casos inválidos

def test_um_valor_zero():
    assert Triangulo(0, 4, 5).tipo() == "Inválido"

def test_um_valor_negativo():
    assert Triangulo(-3, 4, 5).tipo() == "Inválido"

# Soma de dois lados igual ao terceiro

def test_soma_igual_1():
    assert Triangulo(2, 3, 5).tipo() == "Inválido"

def test_soma_igual_2():
    assert Triangulo(3, 5, 2).tipo() == "Inválido"

def test_soma_igual_3():
    assert Triangulo(5, 2, 3).tipo() == "Inválido"

# Soma de dois lados menor que o terceiro

def test_soma_menor_1():
    assert Triangulo(2, 3, 6).tipo() == "Inválido"

def test_soma_menor_2():
    assert Triangulo(3, 6, 2).tipo() == "Inválido"

def test_soma_menor_3():
    assert Triangulo(6, 2, 3).tipo() == "Inválido"

# Todos os valores iguais a zero

def test_todos_zero():
    assert Triangulo(0, 0, 0).tipo() == "Inválido"
