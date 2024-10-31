/* Escribir un programa que calcule la media de una cantidad de números introducidos por
teclado do-while. */

#include <iostream>
using namespace std;

int main(){
    double media, ingresado, sumaTotal=0, count=0;

    do{
     cout << "Dame numeros y calcule la media (0 para terminar)"<<endl;
     cin >> ingresado;
     sumaTotal=sumaTotal+ingresado;
     count++;
    }while (ingresado!=0);
    count--;
    media = sumaTotal/count;

    cout << "La media es " << media << " de " << count << " numeros." << endl; 

}