import pytest
from app_apart_hotel import calcular_apart_hotel

# Casos Válidos combinando classes válidas
@pytest.mark.parametrize("apartamento, inquilinos, limite, esperado", [
    (50, 2, 3000, (200.0, "mensal")),       # A de 1 dorm, I<=2, limite mensal
    (150, 3, 7500, (450.0, "bimestral")),    # A de 2 dorm, I<=3, limite bimestral
    (200, 5, 15000, (500.0, "semestral")),   # A de 2 dorm, I>3, limite semestral
    (400, 2, 2000, (400.0, "mensal")),       # A de 3 dorm, I<=3, limite mensal
    (450, 5, 6000, (750.0, "bimestral")),    # A de 3 dorm, 4<=I<=6, limite bimestral
    (490, 8, 25000, (800.0, "semestral")),   # A de 3 dorm, I>=7, limite semestral
])

def test_classes_validas(apartamento, inquilinos, limite, esperado):
    assert calcular_apart_hotel(apartamento, inquilinos, limite) == esperado

# Casos de erro por dados inválidos de entrada ou regras de negócio violadas
@pytest.mark.parametrize("apartamento, inquilinos, limite", [
    (0, 2, 5000),         # Apartamento inválido (< 1)
    (501, 2, 5000),       # Apartamento inválido (> 500)
    (100, 0, 5000),       # Inquilinos inválido (< 1)
    (100, 10, 5000),      # Inquilinos inválido (> 9)
    (100, 2, 0),          # Limite inválido (< 1)
    (100, 2, 100001),     # Limite inválido (> 100000)
    (50, 3, 5000),        # RN1 Violada: Apartamento tipo 1 com 3 inquilinos
    (200, 7, 5000),       # RN2 Violada: Apartamento tipo 2 com 7 inquilinos
])

def test_classes_invalidas(apartamento, inquilinos, limite):
    with pytest.raises(ValueError):
        calcular_apart_hotel(apartamento, inquilinos, limite)
