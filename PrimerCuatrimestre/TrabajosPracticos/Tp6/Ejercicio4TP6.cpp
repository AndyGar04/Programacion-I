/* Cargar un arreglo de 10 lugares con números aleatorios (usar el rango que quiera), ordenarlo
de manera ascendente eligiendo uno de los métodos de ordenación anteriores y realizar la
búsqueda de un número ingresado por el usuario, usando la búsqueda binaria. */

#include <iostream>
#include <ctime>
using namespace std;

void OrdenInsercionIntercambios(int nums[], int c) {
    int pos, tmp;
    // ALGORITMO DE ORDENAMIENTO POR INSERCION CON INTERCAMBIOS
    for (int i = 1; i < c; i++) {
        pos = i;
        while ((pos > 0) && (nums[pos - 1] < nums[pos])) {
            // INTERCAMBIAMOS CON LA VARIABLE TEMPORAL
            tmp = nums[pos];
            nums[pos] = nums[pos - 1];
            nums[pos - 1] = tmp;
            pos--;
        }
    }
    // IMPRIMO EN ORDEN DESCENDENTE ORDENADO
    cout << "Arreglo Ordenado: ";
    for (int j = 0; j < c; j++) {
        cout << nums[j] << " ";
    }
    cout << endl;
}

void BusquedaBinaria(int nums[], int c) {
    int mitad, primero, ultimo, n;
    int x = -1;
    primero = 0;
    ultimo = c - 1;

    cout << "Ingresa el numero a buscar: ";
    cin >> n;

    while ((primero <= ultimo) && x == -1) {
        mitad = (primero + ultimo) / 2;
        cout << "Mitad: " << mitad << "\t";

        if (n == nums[mitad]) {
            x = mitad;
        } else if (n < nums[mitad]) {
            ultimo = mitad - 1;
        } else {
            primero = mitad + 1;
        }
    }

    cout << endl;

    if (x != -1) {
        cout << "El numero se encuentra en el vector, en la posicion " << x << endl;
    } else {
        cout << "El numero no se encuentra en el vector" << endl;
    }
}

int main() {
    int n = 10;
    int Arreglo[n];
    srand(time(NULL));

    cout << "Arreglo original: ";
    for (int i = 0; i < n; i++) {
        Arreglo[i] = rand() % 10 + 1;
        cout << Arreglo[i] << " ";
    }
    cout << endl;

    OrdenInsercionIntercambios(Arreglo, n);
    BusquedaBinaria(Arreglo, n);

    return 0;
}
