/* Escribir un programa que complete una matriz de 5x5 con la suma de sus correspondientes
índices. Ejemplo en la posición fila 3 columna 2 debe guardar el número 5. */

#include <iostream>
using namespace std;

int main(){

 int fila = 5;
 int col = 5;

 int Matriz[fila][col];
 
 for (int i = 0 ; i < fila ; i++){
     for (int j = 0 ; j < col ; j++){
         Matriz[i][j] = i + j;
     }
    }

 for (int i = 0 ; i < fila ; i++){
     for (int j = 0 ; j < col ; j++){
         cout << Matriz[i][j] << " ";
     }
     cout << endl;
    }

}