/* Escribe una función que reciba dos números enteros y devuelva su suma. */
#include <iostream>
using namespace std;

void suma(int x, int y){

    cout << "La suma es: " << x+y <<endl;

}

int main(){

int num1, num2;

cout << "Dame un numero: ";
cin >> num1;
cout << "Dame otro numero: ";
cin >> num2;

suma(num1,num2);

}