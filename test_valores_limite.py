import pytest
from app_apart_hotel import calcular_apart_hotel

# Amostra de testes focados nas bordas de transição de dados e regras
@pytest.mark.parametrize("apartamento, inquilinos, limite, esperado", [
    (1, 1, 1, (100.0, "mensal")),              # Limite mínimo absoluto do sistema
    (100, 2, 4999, (200.0, "mensal")),         # Limite superior da RN1 e limite inferior do cartão
    (101, 3, 5000, (450.0, "bimestral")),      # Transição RN1->RN2 e transição limite mensal->bimestral
    (300, 4, 10000, (400.0, "bimestral")),     # Limite superior da RN2 e limite superior bimestral
    (301, 6, 10001, (900.0, "semestral")),     # Transição RN2->RN3 e transição bimestral->semestral
    (500, 9, 100000, (900.0, "semestral")),    # Limite máximo absoluto válido do sistema
])

def test_valores_limite_validos(apartamento, inquilinos, limite, esperado):
    assert calcular_apart_hotel(apartamento, inquilinos, limite) == esperado

@pytest.mark.parametrize("apartamento, inquilinos, limite", [
    (0, 2, 5000),         # Fora do limite inferior (apartamento)
    (501, 2, 5000),       # Fora do limite superior (apartamento)
    (100, 0, 5000),       # Fora do limite inferior (inquilinos)
    (100, 10, 5000),      # Fora do limite superior (inquilinos)
    (100, 2, 0),          # Fora do limite inferior (cartão)
    (100, 2, 100001),     # Fora do limite superior (cartão)
    (100, 3, 5000),       # Justamente na fronteira de invalidação da RN1 (Máx 2)
    (300, 7, 5000),       # Justamente na fronteira de invalidação da RN2 (Máx 6)
])

def test_valores_limite_invalidos(apartamento, inquilinos, limite):
    with pytest.raises(ValueError):
        calcular_apart_hotel(apartamento, inquilinos, limite)
