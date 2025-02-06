# 1
def suma_digitos(numero: int) -> int:
    return sum(int(digito) for digito in str(abs(numero)))


print(suma_digitos(1234))  # respuesta: 10


# 2
def contar_vocales(cadena: str) -> int:
    vocales = "aeiou"
    return sum(1 for letra in cadena.lower() if letra in vocales)


print(contar_vocales("Hola Mundo"))  # respuesta: 4

# 3
def es_palindromo(cadena: str) -> str:
    cadena_limpia = ''.join(c for c in cadena.lower() if c.isalnum())
    return "Si" if cadena_limpia == cadena_limpia[::-1] else "No"

print(es_palindromo("anita lava la tina"))  # Respuesta: Si
