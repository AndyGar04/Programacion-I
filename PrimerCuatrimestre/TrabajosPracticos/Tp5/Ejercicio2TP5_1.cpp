/* Dado un arreglo de tamaño N=16 cargado aleatoriamente. Copiar sus valores en una matriz
de 4x4. */

#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int main(){
    int Array[16];
    int Matriz[4][4];
    int var=0;

    srand(time(NULL));

    for (int i=0; i<16;i++){
        Array[i]=rand()%6+1;
    }

   cout << "Array recorrido: ";

    for(int i=0; i<16; i++){
        cout << " " << Array[i] <<" ";
    } 

    cout << endl;

    for (int i=0;i<4;i++){
        for (int j=0;j<4;j++){
            Matriz[i][j]= Array[var+j];
            cout << var+j;
        }
        var=var+4;
    }

    cout << "Recorrida como anteriormente Array ascendentes"<< endl;

  for (int fila = 0 ; fila < 4 ; fila++){
     for (int col = 0 ; col < 4 ; col++){
        cout << " " << Matriz[fila][col] << " ";
     }
     cout << endl;
    }
}