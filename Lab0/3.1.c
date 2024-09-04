4.3 ideal 
//YURI KATERINE SERRANO # diego casas
#include <stdio.h>

// Función para calcular el IMC
float calcularIMC(float peso, float altura) {
    return peso / (altura * altura);
}

// Función para clasificar el nivel de peso
int niveldepeso(float IMC) {
    if (IMC < 18.5) {
        return 1;  // Bajo peso
    } else if (IMC >= 18.5 && IMC <= 24.9) {
        return 2;  // Peso normal
    } else if (IMC >= 25 && IMC <= 29.9) {
        return 3;  // Sobrepeso
    } else if (IMC >= 30 && IMC <= 39.9) {
        return 4;  // Obesidad tipo I
    } else if (IMC >= 40 && IMC <= 49.9) {
        return 5;  // Obesidad tipo II
    } else {
        return 6;  // Obesidad tipo III
    }
}

// Función para calcular el peso ideal
float calcularPesoIdeal(float altura) {
    return 22.2 * (altura * altura);  // 22.2 es el punto medio del rango de IMC normal (18.5-24.9)
}

int main() {
    float peso, altura, IMC, peso_ideal;
    int nivel;

    // Pedir al usuario el peso y la altura
    printf("Ingrese el peso (kg): ");
    scanf("%f", &peso);
    printf("Ingrese su estatura (m): ");
    scanf("%f", &altura);

    // Calcular el IMC y determinar el nivel de peso
    IMC = calcularIMC(peso, altura);
    nivel = niveldepeso(IMC);

    // Imprimir el resultado
    printf("Su IMC es: %.2f\n", IMC);

    // Mostrar el nivel de peso
    switch (nivel) {
        case 1: printf("Su nivel de peso es: Bajo peso\n"); break;
        case 2: printf("Su nivel de peso es: Peso normal\n"); break;
        case 3: printf("Su nivel de peso es: Sobrepeso\n"); break;
        case 4: printf("Su nivel de peso es: Obesidad tipo I\n"); break;
        case 5: printf("Su nivel de peso es: Obesidad tipo II\n"); break;
        case 6: printf("Su nivel de peso es: Obesidad tipo III\n"); break;
    }

    // Verificar si el usuario está en bajo peso, sobrepeso u obesidad
    if (nivel != 2) {
        peso_ideal = calcularPesoIdeal(altura);
        printf("Para lograr un peso normal, su peso ideal debería ser aproximadamente: %.2f kg\n", peso_ideal);
    }

    return 0;
}