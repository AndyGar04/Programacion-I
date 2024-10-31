/* Un tramo; Modifica columna; Ascendente; Un inicio */

#include <iostream>
using namespace std;

int main(){
    int n=6;
    int Matriz[n][n];

    for (int fila=0; fila < n; fila++){
        for (int columna=0; columna < n; columna++){
          Matriz[fila][columna] = columna;  
        }
    }

    for (int fila=0; fila < n; fila++){
       for (int columna=0; columna < n; columna++){
          cout << " " << Matriz[fila][columna] << " ";  
        }
      cout << endl;  
    }
     
    cout << endl;  

    for (int columna=0; columna<n; columna++){
      for (int fila=0; fila<n; fila++){
        cout << " " << Matriz[fila][columna] << " ";
      }
      cout << endl;
    }

}