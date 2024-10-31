/* Escribir un programa que le pida al usuario ingresar una palabra de no más de 10 letras, luego
debe llenar un arreglo con las letras de la palabra desde atrás hacia delante y en caso de que
queden huecos en el arreglo debe llenarse con *. Luego mostrar en consola el contenido de
dicho arreglo.
Ejemplo: Si se ingresa la palabra trabajo, el arreglo debe quedar de la siguiente manera ojabart***. */

#include <iostream>
#include <cstring>
using namespace std;

int main() {
    const int Max = 10; // Tamaño del arreglo
    char palabra[Max + 1]; // Más uno para el carácter nulo
    char arreglo[Max];

    // Pedir al usuario que ingrese una palabra
    cout << "Ingrese una palabra de no más de 10 letras: " << endl;
    cin >> palabra;

    // Obtener la longitud de la palabra
    int longitud = strlen(palabra);

    // Llenar el arreglo con las letras de la palabra en orden inverso
    for (int i = 0; i < Max; ++i) {
        if (i < longitud) {
            arreglo[i] = palabra[longitud - 1 - i];
        } else {
            arreglo[i] = '*'; // Llenar con asteriscos si no hay más letras
        }
    }

    // Mostrar el contenido del arreglo
    cout << "Contenido del arreglo: ";
    for (int i = 0; i < Max; ++i) {
        cout << arreglo[i];
    }
    cout << endl;
}
