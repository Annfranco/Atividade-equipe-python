import pytest

from Atividade.models.endereco import Endereco

@pytest.fixture
def endereco_valido():
    endereco = Endereco("Rua A", "210", "Terreo", "41000-210", "Salvador")
    return endereco

def test_endereco_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == "Rua A"

def test_endereco_numero_valido(endereco_valido):
    assert endereco_valido.numero == "210"

def test_endereco_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == "Terreo"

def test_endereco_cep_valido(endereco_valido):
    assert endereco_valido.cep == "41000-210"

def test_endereco_cidade_valido(endereco_valido):
    assert endereco_valido.cidade == "Salvador"

def test_endereco_logradouro_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Endereco("", "210", "Terreo", "4100-210", "Salvador")

def test_endereco_logradouro_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está invalido."):
        Endereco(1165, "210", "Terreo", "4100-210", "Salvador")

def test_endereco_numero_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Endereco("Rua A", "", "Terreo", "4100-210", "Salvador")

def test_endereco_numero_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está invalido."):
        Endereco("Rua A", 111, "Terreo", "4100-210", "Salvador")

def test_endereco_complemento_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Endereco("Rua A", "210", "", "4100-210", "Salvador")

def test_endereco_complemento_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está invalido."):
        Endereco("Rua A", "210", 111, "4100-210", "Salvador")

def test_endereco_cep_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Endereco("Rua A", "210", "Terreo", "", "Salvador")

def test_endereco_cep_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está invalido."):
        Endereco("Rua A", "210", "Terreo", 111, "Salvador")

def test_endereco_cidade_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Endereco("Rua A", "210", "Terreo", "4100-210", "")

def test_endereco_cidade_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está invalido."):
        Endereco("Rua A", "210", "Terreo", "4100-210", 111)