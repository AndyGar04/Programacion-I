/* Escribir un programa que pida al usuario un número y determine si es primo o no utilizando
un bucle while. */

#include <iostream>
using namespace std;

int main(){
    int n, Cont, Multi;
    Cont=1;
    Multi=0;
    cout << " Dame un numero y te dire si es primo o no " << endl;
    cin >> n;

    cout << "Es divicible por ";

    while (n > Cont){
        if (n % Cont == 0){
        Multi++;
        cout << Cont << " , ";
        }
        Cont++;
    }

    cout << "y por " << n << endl;

    if (Multi > 2){
       cout << "El numero no es primo";
    }else{
        cout << "El numero es primo";
    }
}