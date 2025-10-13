import re

class Email:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class Person:
    def __init__(self, id: int, name: str, age: int, emails: list):
        self.id = id
        self.name = name
        self.age = age
        self.emails = emails


class PersonDAO:
    def save(self, p: Person) -> None:
        """Simula salvar a pessoa (não implementado neste exercício)."""
        pass

    def isValidToInclude(self, p: Person) -> list[str]:
        erros = []

        partes_nome = p.name.strip().split()
        if len(partes_nome) < 2 or not all(parte.isalpha() for parte in partes_nome):
            erros.append("Nome deve conter ao menos duas partes com letras apenas.")

        if not (1 <= p.age <= 200):
            erros.append("Idade deve estar no intervalo [1, 200].")

        if not p.emails or len(p.emails) == 0:
            erros.append("Pessoa deve possuir ao menos um e-mail.")
        else:
            padrao_email = re.compile(r"^[^@]+@[^@]+\.[^@]+$")
            for email in p.emails:
                if not padrao_email.match(email.name):
                    erros.append(f"E-mail inválido: {email.name}")

        return erros
