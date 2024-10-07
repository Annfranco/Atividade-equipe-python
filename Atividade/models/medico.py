from Atividade.models.endereco import Endereco
from Atividade.models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm: str, endereco: Endereco) -> None:
        super().__init__(self._verificar_nome(nome), self._verificar_telefone(telefone), 
                         self._verificar_email(email), endereco)

        self.crm = self._verificar_crm(crm)

    def _verificar_nome(self, nome):

        self._verificar_nome_tipo_invalido(nome)
        self._verificar_nome_vazio(nome)

        self.nome = nome
        return self.nome
    
    
    def _verificar_telefone(self, telefone):

        self._verificar_telefone_vazio(telefone)

        self.telefone = telefone
        return self.telefone
    
    def _verificar_email(self, email):

        self._verificar_email_invalido(email)
        self._verificar_email_vazio(email)

        self.email = email
        return self.email
    
    def _verificar_crm(self, crm):

        self._verificar_crm_vazio(crm)

        self.crm = crm
        return self.crm
    
    def _verificar_nome_tipo_invalido(self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser um texto.")
        
    def _verificar_nome_vazio(self, nome):
        if not nome.strip():
            raise TypeError("O nome não deve estar vazio.")
        
    def _verificar_telefone_vazio(self, telefone):
        if not telefone.strip():
            raise TypeError("O telefone não deve estar vazio.")
        return telefone
        
    def _verificar_email_vazio(self, email):
        if not email.strip():
            raise TypeError("O e-mail não deve estar vazio.")
    
    def _verificar_email_invalido(self, email):
        if not isinstance(email, str):
            raise TypeError("O e-mail deve ser um texto.")
        
    def _verificar_crm_vazio(self, crm):
        if not crm.strip():
            raise TypeError("O CRM não deve estar vazio.")

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nNome - {self.nome}"
                f"\nTelefone - {self.telefone}"
                F"\nE-mail - {self.email}"
                f"\nCRM - {self.crm}"
                f"\nEndereço - {self.endereco}")

