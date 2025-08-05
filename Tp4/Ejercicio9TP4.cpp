/* Escribir un programa que al ingresar el lado de un cuadrado dibuje en consola un cuadrado
con el carácter “*”. Por ejemplo, al ingresar lado = 4, el dibujo debe quedar de la siguiente
manera. */

#include <iostream>
using namespace std;

int main(){
    int Dim;
    cout << "Dame un numero y te hare un cuadrado de * de esa dimension"<<endl;
    cin >> Dim;

    for(int i=0;i<Dim;i++){
       for(int j=0;j<Dim;j++){
        cout << " * "; } 
      cout << " " << endl;  
    }
}