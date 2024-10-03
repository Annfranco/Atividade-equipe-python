import pytest
from Atividade.models.funcionario import Funcionario
from Atividade.models.medico import Medico
from Atividade.models.endereco import Endereco

@pytest.fixture
def medico_valido():
    medico = Medico("Marta", "(71)91111-0000", "marta@gmail.com", "123456",
                    Endereco("Rua Mago", "123", "N/D", "400.456.123", "Salvador"))
    return medico

def test_nome_valido(medico_valido):
    assert medico_valido.nome == "Marta"

def test_telefone_valido(medico_valido):
    assert medico_valido.telefone == "(71)91111-0000"

def test_email_valido(medico_valido):
    assert medico_valido.email == "marta@gmail.com"

def test_crm_valido(medico_valido):
    assert medico_valido.crm == "123456"

def test_logradouro_valido(medico_valido):
    assert medico_valido.endereco.logradouro == "Rua Mago"

def test_numero_valido(medico_valido):
    assert medico_valido.endereco.numero == "123"

def test_complemento_valido(medico_valido):
    assert medico_valido.endereco.complemento == "N/D"

def test_cep_valido(medico_valido):
    assert medico_valido.endereco.cep == "400.456.123"

def test_cidade_valido(medico_valido):
    assert medico_valido.endereco.cidade == "Salvador"