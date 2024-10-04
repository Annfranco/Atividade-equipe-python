import pytest
from Atividade.models.Endereco import Endereco
from Atividade.models.Funcionario import Funcionario
from Atividade.models.Engenheiro import Engenheiro

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