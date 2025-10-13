# 💼 Calculadora de Salário, Tipos de Triângulo e Conjunto de Classes — TDD com Python e Pytest

## 🧪 Desenvolvimento com TDD

O projeto foi desenvolvido seguindo as três etapas clássicas do Test Driven Development (TDD):

1.  **🔴 Red**: Criação de um teste que inicialmente falha.
2.  **🟢 Green**: Implementação do código mínimo para o teste passar.
3.  **🧹 Refactor**: Refatoração do código mantendo todos os testes verdes.

Todos os cenários de cálculo foram validados com **Pytest**.

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone [https://github.com/YanYamim/lab_V_testes.git]
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
Se o arquivo requirements.txt não existir, instale manualmente:

pip install pytest
```

### 🧾 Executando os Testes
```bash
Para rodar todos os testes:

pytest -v
O parâmetro -v (verbose) exibe o nome e o status de cada caso de teste.

Se quiser verificar cobertura de código:

pytest --cov=src --cov-report=term-missing
```

### 📊 Exemplo de saída
```bash
====================================================================================== 28 passed in 0.07s ======================================================================================
(venv) yanyamim@Nootezin:~/Documentos/faculdade/lab_v_testes/lab_V_testes$ pytest -v
===================================================================================== test session starts ======================================================================================
platform linux -- Python 3.12.11, pytest-8.4.2, pluggy-1.6.0 -- /home/yanyamim/Documentos/faculdade/lab_v_testes/lab_V_testes/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/yanyamim/Documentos/faculdade/lab_v_testes/lab_V_testes
collected 28 items                                                                                                                                                                             

test_classes.py::test_nome_invalido_um_sobrenome PASSED                                                                                                                                  [  3%]
test_classes.py::test_nome_invalido_com_numeros PASSED                                                                                                                                   [  7%]
test_classes.py::test_idade_fora_do_intervalo PASSED                                                                                                                                     [ 10%]
test_classes.py::test_sem_email_associado PASSED                                                                                                                                         [ 14%]
test_classes.py::test_email_invalido_formato PASSED                                                                                                                                      [ 17%]
test_classes.py::test_todos_campos_validos PASSED                                                                                                                                        [ 21%]
test_salario.py::test_desenvolvedor_salario_maior_ou_igual_3000 PASSED                                                                                                                   [ 25%]
test_salario.py::test_desenvolvedor_salario_menor_3000 PASSED                                                                                                                            [ 28%]
test_salario.py::test_dba_salario_maior_ou_igual_2000 PASSED                                                                                                                             [ 32%]
test_salario.py::test_dba_salario_menor_2000 PASSED                                                                                                                                      [ 35%]
test_salario.py::test_testador_salario_maior_ou_igual_2000 PASSED                                                                                                                        [ 39%]
test_salario.py::test_testador_salario_menor_2000 PASSED                                                                                                                                 [ 42%]
test_salario.py::test_gerente_salario_maior_ou_igual_5000 PASSED                                                                                                                         [ 46%]
test_salario.py::test_gerente_salario_menor_5000 PASSED                                                                                                                                  [ 50%]
test_triangulo.py::test_escaleno_valido PASSED                                                                                                                                           [ 53%]
test_triangulo.py::test_isosceles_valido_1 PASSED                                                                                                                                        [ 57%]
test_triangulo.py::test_isosceles_valido_2 PASSED                                                                                                                                        [ 60%]
test_triangulo.py::test_isosceles_valido_3 PASSED                                                                                                                                        [ 64%]
test_triangulo.py::test_equilatero_valido PASSED                                                                                                                                         [ 67%]
test_triangulo.py::test_um_valor_zero PASSED                                                                                                                                             [ 71%]
test_triangulo.py::test_um_valor_negativo PASSED                                                                                                                                         [ 75%]
test_triangulo.py::test_soma_igual_1 PASSED                                                                                                                                              [ 78%]
test_triangulo.py::test_soma_igual_2 PASSED                                                                                                                                              [ 82%]
test_triangulo.py::test_soma_igual_3 PASSED                                                                                                                                              [ 85%]
test_triangulo.py::test_soma_menor_1 PASSED                                                                                                                                              [ 89%]
test_triangulo.py::test_soma_menor_2 PASSED                                                                                                                                              [ 92%]
test_triangulo.py::test_soma_menor_3 PASSED                                                                                                                                              [ 96%]
test_triangulo.py::test_todos_zero PASSED                                                                                                                                                [100%]

====================================================================================== 28 passed in 0.13s ======================================================================================
```
### 📦 Build e Execução dos Testes

Este projeto não requer build manual — basta ter o Python 3.11+ instalado e as dependências configuradas.

### 🧪 Test Execution
Os testes são executados via pytest, conforme mostrado acima. Eles garantem que a lógica de cálculo permaneça correta mesmo após refatorações.
