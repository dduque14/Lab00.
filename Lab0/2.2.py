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
cantidad = int(input("Ingrese la cantidad de personas que desea conocer su IMC: "))  # Convertir a entero

# Variables para contar las categorías
bajo_peso = 0
peso_normal = 0
sobrepeso = 0
obesidad_tipo_I = 0
obesidad_tipo_II = 0
obesidad_tipo_III = 0

for i in range(cantidad):
    print(f"\nPersona {i+1}:")
    peso = float(input("Ingrese el peso (kg): "))
    altura = float(input("Ingrese su estatura (m): "))
    
    # Calcular el IMC y determinar el nivel de peso
    IMC = calcularIMC(peso, altura)
    nivel = niveldepeso(IMC)
    
    # Contar cada categoría
    if nivel == "Bajo peso":
        bajo_peso += 1
    elif nivel == "Peso normal":
        peso_normal += 1
    elif nivel == "Sobrepeso":
        sobrepeso += 1
    elif nivel == "Obesidad tipo I":
        obesidad_tipo_I += 1
    elif nivel == "Obesidad tipo II":
        obesidad_tipo_II += 1
    elif nivel == "Obesidad tipo III":
        obesidad_tipo_III += 1
    
    # Imprimir el resultado con dos decimales
    print(f"Su IMC es: {IMC:.2f}")
    print(f"Su nivel de peso es: {nivel}")

# Calcular y mostrar los porcentajes
print("\nPorcentaje de personas en cada categoría:")
print(f"Bajo peso: {bajo_peso / cantidad * 100:.2f}%")
print(f"Peso normal: {peso_normal / cantidad * 100:.2f}%")
print(f"Sobrepeso: {sobrepeso / cantidad * 100:.2f}%")
print(f"Obesidad tipo I: {obesidad_tipo_I / cantidad * 100:.2f}%")
print(f"Obesidad tipo II: {obesidad_tipo_II / cantidad * 100:.2f}%")
print(f"Obesidad tipo III: {obesidad_tipo_III / cantidad * 100:.2f}%")