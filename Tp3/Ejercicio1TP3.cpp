#include <iostream>
using namespace std;

int main(){

    int numero;

    cout << "Dame un numero y te dire si es par o no\n";
    cin >> numero;

    if (numero%2!=0){
      cout << "El numero es impar\n";
    }else{
      cout << "El numero es par\n";
    }
}