# 1
def suma_digitos(numero: int) -> int:
    return sum(int(digito) for digito in str(abs(numero)))


print(suma_digitos(1234))  # respuesta: 10


# 2
def contar_vocales(cadena: str) -> int:
    vocales = "aeiou"
    return sum(1 for letra in cadena.lower() if letra in vocales)


print(contar_vocales("Hola Mundo"))  # respuesta: 4
