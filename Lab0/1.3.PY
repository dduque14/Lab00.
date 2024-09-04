#YURI KATERINE SERRANO

# # Definir la función calc_bmi
def calc_bmi(height, weight):
    bmi = weight / ((height / 100) ** 2)
    return bmi

# Función principal
def main():
    # Pedir al usuario la altura en cm
    height = float(input("Enter your height in cms: "))

    # Pedir al usuario el peso en kg
    weight = float(input("Enter your weight in kgs: "))

    # Llamar a la función calc_bmi
    bmi = calc_bmi(height, weight)

    # Imprimir el resultado
    print(f"Your body mass index is {bmi:.2f} kg/m^2")

# Llamar a la función principal
if __name__ == "__main__":
    main()


