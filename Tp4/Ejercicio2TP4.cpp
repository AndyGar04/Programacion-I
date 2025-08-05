/*Escribir un programa que pida al usuario un número y muestre su tabla de multiplicar
utilizando un bucle for*/

#include <iostream>
using namespace std;

int main(){

    int n;
    cout << "Dame un numero\n";
    cin >> n;

    for(int i=0 ; i<=10 ; i++){
        cout << n << "*" << i << "=" << n*i <<endl;
    }

}