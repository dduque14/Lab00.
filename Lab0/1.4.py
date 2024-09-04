#yuri katerine serrano
# Función para calcular el IMC
def calcularIMC(p, a):
    return p / (a * a)

# Función para clasificar el nivel de peso
def niveldepeso(IMC):
    if IMC < 18.5:
        return "Bajo peso"
    elif 18.5 <= IMC <= 24.9:
        return "Peso normal"
    elif 25 <= IMC <= 29.9:
        return "Sobrepeso"
    elif 30 <= IMC <= 39.9:
        return "Obesidad tipo I"
    elif 40 <= IMC <= 49.9:
        return "Obesidad tipo II"
    else:
        return "Obesidad tipo III"

# Ciclo para ingresar datos de las personas 
for i in range(10):
    print(f"\nPersona {i+1}:")
    peso = float(input("Ingrese el peso (kg): "))
    altura = float(input("Ingrese su estatura (m): "))
    
    # Calcular el IMC y determinar el nivel de peso
    IMC = calcularIMC(peso, altura)
    nivel = niveldepeso(IMC)
    
    # Imprimir el resultado con dos decimales
    print(f"Su IMC es: {IMC:.2f}")
    print(f"Su nivel de peso es: {nivel}")
