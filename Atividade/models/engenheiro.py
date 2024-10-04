from Atividade.models.endereco import Endereco
from Atividade.models.funcionario import Funcionario


class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crea: str, endereco: Endereco) -> None:
        super().__init__(self._verificar_nome_engenheiro(nome), 
                         self._verificar_telefone_engenheiro(telefone), 
                         self._verificar_email_engenheiro(email), endereco)
        self.crea = self._verificar_crea_engenheiro(crea), 


    def _verificar_nome_engenheiro(self, nome):
        self._verificar_nome_tipo_invalido_engenheiro(nome)
        self._verificar_nome_vazio_engenheiro(nome)

        self.nome = nome
        return self.nome
    
    def _verificar_nome_tipo_invalido_engenheiro(self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser um texto")
        
    def _verificar_nome_vazio_engenheiro(self, nome):
         if not nome.strip():
            raise TypeError("O nome não pode estar vazio!")
     
    def _verificar_telefone_engenheiro(self, telefone):
        if not telefone.strip():
            raise TypeError("O número de telefone não pode estar vazio!")
        return telefone
    
    def _verificar_email_engenheiro(self, email):
        if not email.strip():
            raise TypeError("O email não pode estar vazio!")
        return email
    
    def _verificar_crea_engenheiro(self, crea):
        if not crea.strip():
            raise TypeError("O crea não pode estar vazio!")
        return crea
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nNome - {self.nome}"
                f"\nTelefone - {self.telefone}"
                F"\nE-mail - {self.email}"
                f"\nCREA - {self.crea}"
                f"\nEndereço - {self.endereco}")