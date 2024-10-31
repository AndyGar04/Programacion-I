/* Escribir un programa que complete una matriz de 10x10 con el número 1 para los índices que
se encuentren por encima de la diagonal principal y con 0 los que estén por debajo. Los
valores de la diagonal principal deben ir en forma descendente desde el 10 hasta el 1. */

#include <iostream>
#include <cmath>
using namespace std;

int main(){

 const int fila = 10;
 const int col = 10;

 int Matriz[fila][col];
 
 for (int i = 0 ; i < fila ; i++){
     for (int j = 0 ; j < col ; j++){
        if (i==j){
          Matriz[i][j]=10-i;
        }else if (i<j){
          Matriz[i][j]=1; 
        }else{
          Matriz[i][j]=0;
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

