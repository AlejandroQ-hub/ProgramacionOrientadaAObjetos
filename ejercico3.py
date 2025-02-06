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

# 4
def invertir_lista(numeros: str) -> str:
    return ' '.join(numeros.split()[::-1])

print(invertir_lista("1 2 3 4 5"))  # respuesta: 5 4 3 2 1

# 5
def contar_palabras(cadena: str) -> int:
    return len(cadena.split())

print(contar_palabras("Hola mundo desde Python"))
