# 1
def suma_digitos(numero: int) -> int:
    return sum(int(digito) for digito in str(abs(numero)))


print(suma_digitos(1234))  # respuesta: 10


