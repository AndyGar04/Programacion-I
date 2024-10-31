/*
2- Manejo de matrices.
a) Declarar una matriz de 6x6 y cargarla haciendo que el usuario pueda ingresar cada uno de los valores enteros.
b) Mostrar la matriz en forma matricial.
c) Desarrollar la estrategia para poder llevar a cabo el recorrido de la figura, dejando en claro inicio y 
tramos. (No se pide código en este inciso)
d) Escribir el código correspondiente a la estrategia desarrollada en el inciso c.
e) Escribir el código completo con bibliotecas y todo lo necesario para que funcione.
Observaciones:
En cada inciso se debe expresar solo la parte de código correspondiente a lo que se pide, 
excepto en el último donde debe figurar todo lo necesario para que el código sea funcional.

Inicio: Varia col; Descendente; 
Tramo 1: Varia columnas; Descendente; (n-1; lugar variable)
Tramo 2: Varia fila; Descendente; (lugar variable; 0)
*/
#include <iostream>
using namespace std;

int main(){
    int n=6;
    int a=1;
    int matriz[n][n];

    for (int i=0;i<n;i++){
      for (int j=0;j<n;j++){
        //cin << matriz[i][j];
        matriz[i][j]= a++;
      }
    }

    for (int i=0;i<n;i++){
      for (int j=0;j<n;j++){
        //cin << matriz[i][j];
        cout << matriz[i][j] << "\t";
      }
      cout << endl;
    }
    cout << "Otro recorrido" << endl;
    for (int f_in=n-1; f_in>-1; f_in--){
       //tramo 1
       for (int fila=n-1 ;fila>=n-1-f_in;fila--){
          cout << matriz[f_in][fila]<< "\t";
       }
       //tramo 2
       for (int col=f_in;col>-1;col--){
          cout << matriz[col][n-1-f_in]<<"\t";
       }
       
      cout << endl;
    }
}