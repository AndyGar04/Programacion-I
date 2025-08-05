/* Escribir un programa que pida al usuario una palabra y muestre sus letras una por una
utilizando un bucle while.
Ayuda: usar la función length(), propia de la librería string para saber la cantidad de caracteres
de la palabra. Además, saber que si:
string palabra = “ejercicio”;
cout « palabra[3]; //Muestra la letra r porque la primera letra ocupa el lugar 0
cout « palabra[8] //Muestra la letra o porque la última letra es palabra.length() – 1 */

#include <iostream>
#include <string>
using namespace std;

int main(){
    int Cont=0;
    string palabra;
    cout << "Dame una palabra y la desarmare \n";
    cin >> palabra;
    int Cantidad =  palabra.length();

    while (Cont < Cantidad){      
      cout << palabra[Cont]<<endl;
      Cont++;
    }
}