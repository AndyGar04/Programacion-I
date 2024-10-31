/* Escribir un programa que solicite al usuario ingresar un número entero positivo y luego
imprima en la consola una matriz cuadrada con la diagonal principal compuesta por números
en forma ascendente hasta ese valor y los demás elementos de la matriz iguales a cero. Por
ejemplo, si el usuario ingresa el número 6, la matriz resultante debe ser la siguiente: */

#include <iostream>
using namespace std;

int main(){
    int Dim;
    cout << "Dame un numero y te hare un cuadrado de * de esa dimension"<<endl;
    cin >> Dim;
    for(int i=0;i<Dim;i++){

       for(int j=0;j<Dim;j++){

        if (i==j){
            cout << " "<< i+1 <<" ";
        }else{
         cout << " 0 "; } 
        }
      cout << " " << endl;  
    }
}