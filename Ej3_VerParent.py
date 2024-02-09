#3. Verificación de Paréntesis Balanceados:

def parentesis_balancedos(cadena):
    pila = []
    for caracter in cadena:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila or pila.pop() != '(':
                return False
    return not pila, cadena

cadena = "(3, 4, 55, 4, 3, 3)"
resultado, cadena = parentesis_balancedos(cadena)

print("\n****************BIENVENIDO USUARIO************\n")
if resultado:
    print("Los paréntesis en la cadena", cadena, "están balanceados.")
else:
    print("Los paréntesis en la cadena", cadena, "no están balanceados.") 

print("\n************************************************")   