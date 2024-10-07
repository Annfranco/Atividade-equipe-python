import pytest

from Atividade.models.engenheiro import Engenheiro
from Atividade.models.endereco import Endereco

@pytest.fixture
def engenheiro_valido():
    engenheiro = Engenheiro("Ediberto", "(75)97777-6666", "ediberto.engenheiro@gmail.com", "555-05", 
                            Endereco("Artêmia", "155E", "Condomínio", "40700-000", "Feira de Santana"))
    return engenheiro

def test_engenheiro_nome_valido(engenheiro_valido):
    assert engenheiro_valido.nome == "Ediberto"

def test_engenheiro_telefone_valido(engenheiro_valido):
    assert engenheiro_valido.telefone == "(75)97777-6666"

def test_engenheiro_email_valido(engenheiro_valido):
    assert engenheiro_valido.email == "ediberto.engenheiro@gmail.com"

def test_engenheiro_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "555-05"

def test_logradouro_endereco_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.logradouro == "Artêmia"

def test_numero_endereco_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.numero == "155E"

def test_complemento_endereco_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.complemento == "Condomínio"

def test_cep_endereco_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.cep ==  "40700-000"

def test_cidade_endereco_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.cidade == "Feira de Santana"

def test_engenheiro_nome_vazio_mensagem_erro():
    with pytest.raises(TypeError, match= "O nome não pode estar vazio!"):
        Engenheiro("", "(75)97777-6666", "ediberto.engenheiro@gmail.com", "555-05", 
                    Endereco("Artêmia", "155E", "Condomínio", "40700-000", "Feira de Santana"))
        
def test_engenheiro_nome_tipo_invalido_mensagem_erro():
    with pytest.raises(TypeError, match= "O número de telefone não pode estar vazio!"):
        Engenheiro(222, "(75)97777-6666", "ediberto.engenheiro@gmail.com", "555-05", 
                    Endereco("Artêmia", "155E", "Condomínio", "40700-000", "Feira de Santana"))

def test_engenheiro_telefone_vazio_mensagem_erro():
    with pytest.raises(TypeError, match= "O número de telefone não pode estar vazio!"):
        Engenheiro("Ediberto", "", "ediberto.engenheiro@gmail.com", "555-05", 
                    Endereco("Artêmia", "155E", "Condomínio", "40700-000", "Feira de Santana"))     
           
def test_engenheiro_email_vazio_mensagem_erro():
    with pytest.raises(TypeError, match= "O email não pode estar vazio!"):
        Engenheiro("Ediberto", "(75)97777-6666", "", "555-05", 
                    Endereco("Artêmia", "155E", "Condomínio", "40700-000", "Feira de Santana"))   
             
def test_engenheiro_crea_vazio_mensagem_erro():
    with pytest.raises(TypeError, match= "O crea não pode estar vazio!"):
        Engenheiro("Ediberto", "(75)97777-6666", "ediberto.engenheiro@gmail.com", "", 
                    Endereco("Artêmia", "155E", "Condomínio", "40700-000", "Feira de Santana"))        