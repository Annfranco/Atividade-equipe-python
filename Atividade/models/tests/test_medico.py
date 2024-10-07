import pytest

from Atividade.models.medico import Medico
from Atividade.models.endereco import Endereco

@pytest.fixture
def medico_valido():
    medico = Medico("Marta", "(71)91111-1111", "marta@gmail.com", "123456", 
                    Endereco("Rua Santos", "123", "N/D", "123.456.789", "Salvador"))
    return medico

def test_nome_medico_valido(medico_valido):
    assert medico_valido.nome == "Marta"

def test_telefone_medico_valido(medico_valido):
    assert medico_valido.telefone == "(71)91111-1111"

def test_email_medico_valido(medico_valido):
    assert medico_valido.email == "marta@gmail.com"

def test_crm_medico_valido(medico_valido):
    assert medico_valido.crm == "123456"

def test_logradouro_endereco_medico_valido(medico_valido):
    assert medico_valido.endereco.logradouro == "Rua Santos"

def test_numero_endereco_medico_valido(medico_valido):
    assert medico_valido.endereco.numero == "123"

def test_complemento_endereco_medico_valido(medico_valido):
    assert medico_valido.endereco.complemento == "N/D"

def test_cep_endereco_medico_valido(medico_valido):
    assert medico_valido.endereco.cep == "123.456.789"

def test_cidade_endereco_medico_valido(medico_valido):
    assert medico_valido.endereco.cidade == "Salvador"

def test_medico_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome não deve estar vazio."):
        Medico("", "(71)91111-1111", "marta@gmail.com", "123456", 
                    Endereco("Rua Santos", "123", "N/D", "123.456.789", "Salvador"))
        
def test_medico_nome_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome deve ser um texto."):
        Medico(22, "(71)91111-1111", "marta@gmail.com", "123456", 
                    Endereco("Rua Santos", "123", "N/D", "123.456.789", "Salvador"))
        
def test_medico_telefone_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O telefone não deve estar vazio."):
        Medico("Marta", "", "marta@gmail.com", "123456", 
                    Endereco("Rua Santos", "123", "N/D", "123.456.789", "Salvador"))
        
def test_medico_email_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O e-mail não deve estar vazio."):
        Medico("Marta", "(71)91111-1111", "", "123456", 
                    Endereco("Rua Santos", "123", "N/D", "123.456.789", "Salvador"))
        
def test_medico_email_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O e-mail deve ser um texto."):
        Medico("Marta", "(71)91111-1111", 56, "123456", 
                    Endereco("Rua Santos", "123", "N/D", "123.456.789", "Salvador"))
        
def test_medico_crm_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O CRM não deve estar vazio."):
        Medico("Marta", "(71)91111-1111", "marta@gmail.com", "", 
                    Endereco("Rua Santos", "123", "N/D", "123.456.789", "Salvador"))
        
        
