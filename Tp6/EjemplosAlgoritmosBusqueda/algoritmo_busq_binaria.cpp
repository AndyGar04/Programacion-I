#include <iostream>
using namespace std;

int main() {
    int n, mitad, primero, ultimo, x, a[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    primero = 0;
    ultimo = 9;
    x = -1; // Inicializado a -1 para indicar que no se ha encontrado el elemento

    cout << "Ingresa el numero a buscar: ";
    cin >> n;

    while (primero <= ultimo && x == -1) {
        mitad = (primero + ultimo) / 2;
        cout << mitad << "\t";

        if (n == a[mitad])
            x = mitad; // Se almacena el índice del elemento encontrado
        else if (n < a[mitad])
            ultimo = mitad - 1;
        else
            primero = mitad + 1;
    }

    if (x != -1)
        cout << "El numero se encuentra en el vector en la posicion " << x << endl;
    else
        cout << "El numero no se encuentra en el vector" << endl;

    return 0;
}
