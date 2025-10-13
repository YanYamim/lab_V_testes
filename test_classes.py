from ex2_classes import PersonDAO, Person, Email

def test_nome_invalido_um_sobrenome():
    p = Person(id=1, name="Maria", age=25, emails=[Email(1, "maria@email.com")])
    erros = PersonDAO().isValidToInclude(p)
    assert "Nome deve conter ao menos duas partes com letras apenas." in erros

def test_nome_invalido_com_numeros():
    p = Person(id=1, name="Joao123 Silva", age=30, emails=[Email(1, "joao@email.com")])
    erros = PersonDAO().isValidToInclude(p)
    assert "Nome deve conter ao menos duas partes com letras apenas." in erros

def test_idade_fora_do_intervalo():
    p = Person(id=1, name="Ana Clara", age=250, emails=[Email(1, "ana@email.com")])
    erros = PersonDAO().isValidToInclude(p)
    assert "Idade deve estar no intervalo [1, 200]." in erros

def test_sem_email_associado():
    p = Person(id=1, name="Carlos Silva", age=40, emails=[])
    erros = PersonDAO().isValidToInclude(p)
    assert "Pessoa deve possuir ao menos um e-mail." in erros

def test_email_invalido_formato():
    p = Person(id=1, name="Pedro Lima", age=22, emails=[Email(1, "pedroemail.com")])
    erros = PersonDAO().isValidToInclude(p)
    assert "E-mail inválido: pedroemail.com" in erros

def test_todos_campos_validos():
    p = Person(id=1, name="Lucas Pereira", age=30, emails=[Email(1, "lucas@dominio.com")])
    erros = PersonDAO().isValidToInclude(p)
    assert erros == []  # Nenhum erro esperado
