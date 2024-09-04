#YURI KATERINE SERRANO # diego casas
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

# Función para calcular el peso ideal
def calcularPesoIdeal(altura):
    return 22.2 * (altura * altura)  # 22.2 es el punto medio del rango de IMC normal (18.5-24.9)

# Pedir al usuario el peso y la altura
peso = float(input("Ingrese el peso (kg): "))
altura = float(input("Ingrese su estatura (m): "))

# Calcular el IMC y determinar el nivel de peso
IMC = calcularIMC(peso, altura)
nivel = niveldepeso(IMC)

# Imprimir el resultado
print(f"Su IMC es: {IMC:.2f}")
print(f"Su nivel de peso es: {nivel}")

# Verificar si el usuario está en bajo peso, sobrepeso u obesidad
if nivel != "Peso normal":
    peso_ideal = calcularPesoIdeal(altura)
    print(f"Para lograr un peso normal, su peso ideal debería ser aproximadamente: {peso_ideal:.2f} kg")