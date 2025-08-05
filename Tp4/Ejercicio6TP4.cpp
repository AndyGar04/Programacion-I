/* Escribir un programa que calcule el factorial de un número utilizando un bucle for. */

#include <iostream>
using namespace std;

int main(){

    int n, factorial;
    factorial=1;
    cout << " Dame un numero y te dare un factorial \n";
    cin >> n;

    for (int i=1;i<=n;i++){
       factorial=factorial*i;
    }

    cout << "El factorial de " << n << " es " << factorial << endl;

}