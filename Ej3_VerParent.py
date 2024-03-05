#Verificar paréntesis balanceados utilizando una pila:
#Escribir una función en Python que tome una cadena de paréntesis y determine si están balanceados.
#Utilizar una pila para rastrear la apertura y cierre de paréntesis.
def paréntesis_balanceados(cadena):
    pila = []
    for caracter in cadena:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila or pila.pop() != '(':
                return False
    return not pila

# Ejemplo de uso:
cadena = "((()))"
print(paréntesis_balanceados(cadena))  # Output: True
cadena = "(()))"
print(paréntesis_balanceados(cadena))  # Output: False
