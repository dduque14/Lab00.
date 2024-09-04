// Include header file for prototypes of scanf and printf
#include <stdio.h>

// Prototype of calcBmi function
float calcBmi(float h, float w);

// Prototype of printBmiCategory function
void printBmiCategory(float bmi);

// Main function - entry point
int main() {
    // Local variable declaration
    float height;
    float weight;
    float bmi;

    // Ask user for height in cms
    printf("Enter your height in cms: ");
    scanf("%f", &height);

    // Ask user for weight in kgs
    printf("Enter your weight in kgs: ");
    scanf("%f", &weight);

    // Call calcBmi function
    bmi = calcBmi(height, weight);

    // Print result
    printf("Your body mass index is %.2f kg/m^2\n", bmi);

    // Print BMI category
    printBmiCategory(bmi);

    return 0;
}

// Implementation of calcBmi function
float calcBmi(float h, float w) {
    float bmi;

    // Compute body mass index
    bmi = w / ((h / 100.0) * (h / 100.0));
    return bmi;
}

// Implementation of printBmiCategory function
void printBmiCategory(float bmi) {
    if (bmi < 18.5) {
        printf("You are underweight.\n");
    } else if (bmi >= 18.5 && bmi < 24.9) {
        printf("You have a normal weight.\n");
    } else if (bmi >= 25.0 && bmi < 29.9) {
        printf("You are overweight.\n");
    } else {
        printf("You are obese.\n");
    }
}
