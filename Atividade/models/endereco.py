class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = self._verificar_logradouro_endereco(logradouro)
        self.numero = self._verificar_numero_endereco(numero)
        self.complemento = self._verificar_complemento_endereco(complemento)
        self.cep = self._verificar_cep_endereco(cep)
        self.cidade = self._verificar_cidade_endereco(cidade)

    def _verificar_logradouro_endereco(self,logradouro):

        self._verificar_logradouro_invalido(logradouro)
        self._verificar_logradouro_vazio(logradouro)

        self.logradouro = logradouro
        return self.logradouro
    
    def _verificar_numero_endereco(self, numero):

        self._verificar_numero_invalido(numero)
        self._verificar_numero_vazio(numero)

        self.numero = numero
        return self.numero
    
    def _verificar_complemento_endereco(self, complemento):

        self._verificar_complemento_invalido(complemento)
        self._verificar_complemento_vazio(complemento)

        self.complemento = complemento
        return self.complemento
    
    def _verificar_cep_endereco(self, cep):

        self._verificar_cep_invalido(cep)
        self._verificar_cep_vazio(cep)

        self.cep = cep
        return self.cep
    
    def _verificar_cidade_endereco(self, cidade):

        self._verificar_cidade_invalido(cidade)
        self._verificar_cidade_vazio(cidade)

        self.cidade = cidade
        return self.cidade
    
    def _verificar_logradouro_vazio(self, logradouro):
        if not logradouro.strip():
            raise ValueError("O que está sendo solicitado está vazio.")
        return logradouro
        
    def _verificar_logradouro_invalido(self,logradouro):
        if not isinstance(logradouro, str):
            raise TypeError("O que está sendo solicitado está invalido.")
        return logradouro

    def _verificar_numero_vazio(self, numero):
        if not numero.strip():
            raise ValueError("O que está sendo solicitado está vazio.")
        return numero
    
    def _verificar_numero_invalido(self, numero):
        if not isinstance(numero, str):
            raise TypeError("O que está sendo solicitado está invalido.")
        return numero
    
    def _verificar_complemento_vazio(self, complemento):
        if not complemento.strip():
            raise ValueError("O que está sendo solicitado está vazio.")
        return complemento
    
    def _verificar_complemento_invalido(self, complemento):
        if not isinstance(complemento, str):
            raise TypeError("O que está sendo solicitado está invalido.")
        return complemento
    
    def _verificar_cep_vazio(self, cep):
        if not cep.strip():
            raise ValueError("O que está sendo solicitado está vazio.")
        return cep 
    
    def _verificar_cep_invalido(self, cep):
        if not isinstance(cep, str):
            raise TypeError("O que está sendo solicitado está invalido.")
        return cep
    
    def _verificar_cidade_vazio(self, cidade):
        if not cidade.strip():
            raise ValueError("O que está sendo solicitado está vazio.")
        return cidade
    
    def _verificar_cidade_invalido(self, cidade):
        if not isinstance(cidade, str):
            raise TypeError("O que está sendo solicitado está invalido.")
        return cidade
    
    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}"
                f"\nNumero: {self.numero}"
                f"\nComplemento: {self.complemento}"
                f"\nCEP: {self.cep}"
                f"\nCidade: {self.cidade}")