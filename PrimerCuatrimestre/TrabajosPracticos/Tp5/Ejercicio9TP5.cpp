/* 9) Matriz y búsqueda.
a) Escribir un programa que complete una matriz de 10x10 con números aleatorios entre el
1 y el 100. Luego en un arreglo debe guardar el resultado de sumar cada una de las filas,
por lo tanto, va a tener 10 lugares. Mostrar el contenido del arreglo.
b) Debe permitir que el usuario ingrese un número y realizar la búsqueda de este en la matriz.
Si lo encuentra debe mostrar un mensaje que indique que lo encontró y la posición donde
está ubicado en la matriz. Si no lo encuentra que muestre un mensaje de que la búsqueda
finalizo sin éxito. Esto debe repetirse hasta que el usuario ingrese de alguna forma que
no quiere realizar más búsquedas. */


#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main(){

 int fila = 10;
 int col = 10;

 int Matriz[fila][col];
 int Array[fila];

 char buscar = 'y';
 int buscado;
 bool encontrado = false;

 srand(time(NULL));

 for (int i = 0 ; i < fila ; i++){
    Array[i]=0;
     for (int j = 0 ; j < col ; j++){
         Matriz[i][j] = rand() % 100 + 1;
         Array[i] = Array[i] + Matriz[i][j];
     }
    }

 for (int i = 0 ; i < fila ; i++){
     for (int j = 0 ; j < col ; j++){
         cout << Matriz[i][j] << " ";
     }
     cout << endl;
    }

 for (int i=0; i < fila ; i++){
    cout << Array[i] << " , ";
 }   

 cout << endl;

 while (buscar != 'n' || buscar != 'N'){    
 buscado = 0;
 encontrado = false;

 cout << "Que numero desea buscar?" << endl;
 cin >> buscado;

 for (int i = 0 ; i < fila ; i++){
     for (int j = 0 ; j < col ; j++){
         if (Matriz[i][j] == buscado){
            cout << "Se ha encontrado";
            cout << " en la posicion " << i << " " << j << endl;
            encontrado = true;
         }else{
            encontrado = false;
         }
     }
    }

    if (encontrado == false){
      cout << "No se encontro, intente nuevamente" << endl;
    }

    cout << "Quieres buscar de nuevo?(N/Y)" << endl; 
    cin >> buscar;
 }

}