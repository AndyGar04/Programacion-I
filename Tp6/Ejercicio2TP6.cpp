/* Implementa una función que reciba un arreglo de enteros y calcule la suma de todos sus
elementos. */

#include <iostream>
using namespace std;

// Función que recibe un arreglo de enteros y calcula la suma de todos sus elementos
void sumArreglos(const int x[], int y) {
    int sumTotal = 0;
    for (int i = 0; i < y; i++) {
        sumTotal += x[i];
    }
    cout << "La suma es " << sumTotal << endl;
}

int main() {
    int n = 5;
    int Array[] = {1, 2, 3, 4, 5};  // Inicialización correcta del arreglo

    sumArreglos(Array, n);  // Llamada correcta a la función
    
    return 0;
}
