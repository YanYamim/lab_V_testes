class Triangulo:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def eh_valido(self) -> bool:
        """Verifica se os lados formam um triângulo válido."""
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        return (self.a + self.b > self.c) and \
               (self.a + self.c > self.b) and \
               (self.b + self.c > self.a)

    def tipo(self) -> str:
        """Retorna o tipo de triângulo, ou uma mensagem de erro se inválido."""
        if not self.eh_valido():
            return "Inválido"
        if self.a == self.b == self.c:
            return "Equilátero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Isósceles"
        else:
            return "Escaleno"
