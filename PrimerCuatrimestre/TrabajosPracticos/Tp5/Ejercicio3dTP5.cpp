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

    /*for (int col_in = 0; col_in < n; col_in++) {
        if (col_in) {
            // Tramo 1
            for (int fila = 0; fila <; fila++) {
                cout << Matriz[fila][col_in] << "\t";
            }
            // Tramo 2
            for (int col = 0; col > -1; col++) {
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
    }*/   

    for (int Col_in=(n/2)-1; Col_in>-1; Col_in--){
        //tramo 1
        for (int fila=0; fila<=Col_in + (n/2); fila++){
            cout << Matriz[fila][Col_in]<<"\t";
        }
        //tramo 2
        for (int col=Col_in-1; col>-1; col--){
            cout << Matriz[Col_in+(n/2)][col]<<"\t";
        }
        cout << endl;
        //tramo 3
        for (int fila=0; fila<=Col_in + (n/2); fila++){
            cout << Matriz[fila][n-Col_in-1]<<"\t";
        }
        //tramo 4
        for (int col=n-Col_in; col<n; col++){
            cout << Matriz[Col_in+(n/2)][col]<<"\t";
        }
        cout << endl;
    } 
}