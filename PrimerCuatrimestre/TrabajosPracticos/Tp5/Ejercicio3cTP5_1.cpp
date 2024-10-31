/*
  Inicio: Varía filas ; Ascendente ; (0;n-1)
  Tramo 1: Varia fil; Descendente ; (n-1 , lugar variable)
  Tramo 2: Varia col; Descendente ; (lugar variable , 0) 
  Tramo 3: Varia fil; Acendente ; (0 , lugar variable)
  Tramo 4: Varia col; Acendente ; (lugar variable , n-1)  
*/

#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int main(){

    const int n=6;
    int a=1;

    int Matriz[n][n];

    srand(time(NULL));

 for (int fila = 0 ; fila < n ; fila++){
     for (int col = 0 ; col < n ; col++){
        Matriz[fila][col] = a++;
     }
    }

 cout << "Recorrida como anteriormente Array ascendentes"<< endl;

  for (int fila = 0 ; fila < n ; fila++){
     for (int col = 0 ; col < n ; col++){
        cout << " " << Matriz[fila][col] << " ";
     }
     cout << endl;
    }

    cout << "Comienzo de Recorrido...\n";

    for (int col_in = 0; col_in < n; col_in++) {
        if (col_in < (n / 2)) {
            // Tramo 1
            for (int fila = n - 1; fila >= (n / 2) - 1 - col_in; fila--) {
                cout << Matriz[fila][col_in] << "\t";
            }

            // Tramo 2
            for (int col = col_in - 1; col > -1; col--) {
                cout << Matriz[(n / 2) - 1 - col_in][col] << "\t";
            }
            cout << endl;
        } else {
            // Tramo 3
            for (int fila = 0; fila <= n + ((n / 2)-1) - col_in; fila++) {
                cout << Matriz[fila][col_in] << "\t";
            }

            // Tramo 4
            for (int col = col_in + 1; col < n; col++) {
                cout << Matriz[n + ((n / 2) - 1) - col_in][col] << "\t";
            }
            cout << endl;
        }
        cout << endl;
    }    
}                   