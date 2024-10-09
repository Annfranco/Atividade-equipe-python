from Atividade.models.endereco import Endereco
from Atividade.models.funcionario import Funcionario


class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crea: str, endereco: Endereco) -> None:
        super().__init__(self._verificar_nome_engenheiro(nome), 
                         self._verificar_telefone_engenheiro(telefone), 
                         self._verificar_email_engenheiro(email), endereco)
        
        self.crea = self._verificar_crea_engenheiro(crea)

#verificar nome
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

#verificar telefone
    def _verificar_telefone_engenheiro(self, telefone):
        self._verificar_telefone_tipo_invalido(telefone)
        self._verificar_telefone_vazio(telefone)

        self.telefone = telefone
        return self.telefone

    def _verificar_telefone_tipo_invalido(self, telefone):
        if not isinstance (telefone, str):
            raise TypeError("O telefone deve ser um texto")
        
    def _verificar_telefone_vazio(self, telefone):
        if not telefone.strip():
            raise TypeError("O número de telefone não pode estar vazio!")
        
    
#verificar email
    def _verificar_email_engenheiro(self, email):
       self._verficar_email_tipo_invalido(email)
       self._verificar_email_vazio(email)

       self.email = email
       return self.email
    
    def _verficar_email_tipo_invalido(self, email):
        if not isinstance (email, str):
            raise TypeError("O email deve ser um texto")
        
    def _verificar_email_vazio(self, email):
        if not email.strip():
            raise TypeError("O email não pode estar vazio!")
      

#verificar crea
    def _verificar_crea_engenheiro(self, crea):
        self._verificar_crea_tipo_invalido(crea)
        self._verficar_crea_vazio(crea)

        self.crea = crea
        return self.crea
    
    def _verificar_crea_tipo_invalido(self, crea):
        if not isinstance (crea, str):
            raise TypeError("O crea deve ser um texto")
        
    def _verficar_crea_vazio(self, crea):
        if not crea.strip():
            raise TypeError("O crea não pode estar vazio!")
        
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nNome - {self.nome}"
                f"\nTelefone - {self.telefone}"
                F"\nE-mail - {self.email}"
                f"\nCREA - {self.crea}"
                f"\nEndereço - {self.endereco}")