/* Inicio: Varía filas ; Ascendente ; (0;n-1)
 Si es par o impar Tramo 1: Varia col; Ascendente ; (0;n-1)
                   Tramo 2: Varia col; Descendente ; (n-1;0) 
*/

#include <iostream>
using namespace std;

int main(){

    int n=3;

    int Matriz[n][n];
 
 for (int fila = 0 ; fila < n ; fila++){
     for (int col = 0 ; col < n ; col++){
        cout << "Dame numeros y cargare la matriz" << endl;
        cin >> Matriz[fila][col];
     }
    }

 cout << "Recorrida como anteriormente Array ascendentes"<< endl;

  for (int fila = 0 ; fila < n ; fila++){
     for (int col = 0 ; col < n ; col++){
        cout << " " << Matriz[fila][col] << " ";
     }
     cout << endl;
    }

 cout << "Recorrida para este ejercicio"<< endl;   

    for (int filas=0; filas < n; filas++){
        if (filas % 2 == 0){
            //tramo 1
            for (int col=0; col < n; col++){
                cout << Matriz[filas][col]<<"\t";
            }
        }else{
            //tramo 2
            for (int col=n-1; col > -1; col--){
                cout << Matriz[filas][col]<<"\t";
            }            
        }
        cout << endl;
    }

}                   