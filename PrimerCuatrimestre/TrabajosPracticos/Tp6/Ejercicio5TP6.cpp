/* Crea una función que tome dos matrices cuadradas y almacene su suma en una tercera matriz */
#include <iostream>
#include <ctime>
using namespace std;

const int n = 3;

// Cambia la declaración de la función para aceptar matrices bidimensionales
void sumaMatriz(int m1[n][n], int m2[n][n]) {
    int m3[n][n];  // Ajusta la declaración para una matriz de tamaño fijo

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            m3[i][j] = m1[i][j] + m2[i][j];
        }
    }

    cout << "Matriz suma: " << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << m3[i][j] << "\t";
        }
        cout << endl; 
    }
}

int main() {
    int matriz[n][n];
    int matrizn2[n][n];

    srand(time(NULL));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            matriz[i][j] = rand() % 10 + 1;
            matrizn2[i][j] = rand() % 10 + 1;
        }
    }

    cout << "Primera matriz:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << matriz[i][j] << "\t";
        }
        cout << endl;
    }

    cout << endl << "Segunda matriz:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << matrizn2[i][j] << "\t";
        }
        cout << endl;
    }

    sumaMatriz(matriz, matrizn2);

}
