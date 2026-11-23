def calcular_apart_hotel(num_apartamento, num_inquilinos, limite_cartao):

    # Validação de tipos e intervalos gerais de entrada
    if not isinstance(num_apartamento, int) or not (1 <= num_apartamento <= 500):
        raise ValueError("Número do apartamento inválido.")
    
    if not isinstance(num_inquilinos, int) or not (1 <= num_inquilinos <= 9):
        raise ValueError("Número de inquilinos inválido.")
    
    if not isinstance(limite_cartao, int) or not (1 <= limite_cartao <= 100000):
        raise ValueError("Limite do cartão inválido.")

    # Regras para o custo do apartamento [RN1, RN2, RN3]
    if 1 <= num_apartamento <= 100:
    
        if num_inquilinos > 2:
            raise ValueError("Número de inquilinos inadequado para este apartamento.")
        custo = num_inquilinos * 100.0
    
    elif 101 <= num_apartamento <= 300:
    
        if num_inquilinos > 6:
            raise ValueError("Número de inquilinos inadequado para este apartamento.")
        if num_inquilinos <= 3:
            custo = num_inquilinos * 150.0
        else:
            custo = num_inquilinos * 100.0
    
    else:  # 301 a 500
    
        if num_inquilinos <= 3:
            custo = num_inquilinos * 200.0
        elif 4 <= num_inquilinos <= 6:
            custo = num_inquilinos * 150.0
        else:
            custo = num_inquilinos * 100.0

    # Regras para frequência de pagamento [RN4, RN5, RN6]
    if limite_cartao < 5000:
        frequencia = "mensal"
    elif 5000 <= limite_cartao <= 10000:
        frequencia = "bimestral"
    else:
        frequencia = "semestral"

    return custo, frequencia