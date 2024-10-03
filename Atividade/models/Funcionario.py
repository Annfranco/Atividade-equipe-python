from abc import abstractmethod
from Atividade.models.Endereco import Endereco

class Funcionario(abstractmethod):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email)
        self.endereco = endereco

    def __str__(self) -> str:
        return(f"== Funcionário =="
               f"\nNome - {self.nome}"
               f"\nTelefone - {self.telefone}"
               f"\nE-mail - {self.email}"
               f"\n== Endereço ==")