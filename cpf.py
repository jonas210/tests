cpf = "788.710.790-35"
cpf_limpo = "".join(c for c in cpf if c.isdigit())

nove_digitos = [int(c) for c in cpf_limpo[:9]]

soma = sum(n * p for n, p in zip(nove_digitos, range(10, 1, -1)))

digito1 = (soma * 10) % 11

#Primeiro digito verificador
print(0 if digito1 > 9 else digito1)

dez_digitos = [int(c) for c in cpf_limpo[:10]]

soma = sum(n * p for n, p in zip(dez_digitos, range(11, 1, -1)))

digito2 = (soma * 10) % 11

#Segundo digito verificador
print(0 if digito2 > 9 else digito2)