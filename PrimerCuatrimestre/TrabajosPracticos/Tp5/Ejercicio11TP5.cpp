/* Escribe un programa donde la cantidad de filas y columnas de la matriz estén definidas por
constantes distintas. Luego, completa los elementos de la matriz siguiendo estas reglas: si la
suma de los índices de un lugar es par, ese lugar se llenará con la raíz cuadrada de la suma de
los índices. En caso de que la suma de los índices sea impar, ese lugar se llenará con un valor
de 0. */

#include <iostream>
#include <cmath>
using namespace std;

int main(){

 const int fila = 6;
 const int col = 4;

 int Matriz[fila][col];
 
 for (int i = 0 ; i < fila ; i++){
     for (int j = 0 ; j < col ; j++){
        if ((i+j)%2 == 0){
         Matriz[i][j] = sqrt(i + j);
        } else {
         Matriz[i][j] = 0;   
        }
     }
    }

 for (int i = 0 ; i < fila ; i++){
     for (int j = 0 ; j < col ; j++){
         cout << Matriz[i][j] << " ";
     }
     cout << endl;
    }

}

