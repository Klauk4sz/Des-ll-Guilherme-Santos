def validar_cpf(cpf: str) -> bool:
    # Remover caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se o CPF possui 11 dígitos
    if len(cpf) != 11:
        print("CPF inválido: deve conter 11 dígitos.")
        return False

    # Extrair os 9 primeiros dígitos do CPF
    cpf_base = cpf[:9]
    print("Primeiros 9 dígitos:", cpf_base)

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf_base[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    primeiro_dv = 0 if resto < 2 else 11 - resto
    print("Primeiro DV calculado:", primeiro_dv)

    # Cálculo do segundo dígito verificador
    cpf_base += str(primeiro_dv)
    soma = sum(int(cpf_base[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    segundo_dv = 0 if resto < 2 else 11 - resto
    print("Segundo DV calculado:", segundo_dv)

    # Verificação dos dígitos verificadores
    validacao = cpf.endswith(f"{primeiro_dv}{segundo_dv}")
    print("CPF fornecido:", cpf)
    print("Dígitos verificadores calculados:", f"{primeiro_dv}{segundo_dv}")
    print("CPF é válido!" if validacao else "CPF é inválido!")
    return validacao

# Solicitar que o usuário digite um CPF
cpf_usuario = input("Digite um CPF para validar: ")
validar_cpf(cpf_usuario)
