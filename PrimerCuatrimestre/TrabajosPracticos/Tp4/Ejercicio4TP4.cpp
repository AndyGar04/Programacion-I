/* Escribir un programa que pida al usuario un número y muestre sus divisores utilizando un
bucle for */

#include <iostream>
using namespace std;

int main(){

    int n;
    cout << "Dame un numero y te dire sus divisores\n";
    cin >> n;

    for (int i=n ;i<=n; i--){
        if (n % i == 0){
            cout << i << " es divisor \n"; 
        }
    }
}