from Atividade.models.Endereco import Endereco
from Atividade.models.Funcionario import Funcionario


class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crea: str, endereco: Endereco) -> None:
        super().__init__(self._verificar_nome_engenheiro(nome), 
                         self._verificar_telefone_engenheiro(telefone), 
                         self._verificar_email_engenheiro(email), 
                         self._verificar_crea_engenheiro(crea), 
                         endereco)

    def _verificar_nome_engenheiro(self, nome):
        if nome == "":
            raise ValueError("O nome não pode estar vazio!")
        return nome
    
    def _verificar_telefone_engenheiro(self, telefone):
        if telefone == "":
            raise ValueError("O número de telefone não pode estar vazio!")
        return telefone
    
    def _verificar_email_engenheiro(self, email):
        if email == "":
            raise ValueError("O email não pode estar vazio!")
        return email
    
    def _verificar_crea_engenheiro(self, crea):
        if crea == "":
            raise ValueError("O crea não pode estar vazio!")
        return crea