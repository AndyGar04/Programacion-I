/* 8) Escribe una función llamada "intercambiar" que reciba dos variables de tipo string y las
intercambie entre sí. */
#include <iostream>
#include <string>
using namespace std;

void intercambiar(string& palabran1, string& palabran2) {
    string aux = palabran1;
    palabran1 = palabran2;
    palabran2 = aux;
}

int main() {
    string palabra1, palabra2;
    cout << "Dame una palabra: ";
    cin >> palabra1;
    cout << "Dame otra palabra: ";
    cin >> palabra2;
    
    intercambiar(palabra1, palabra2);
    
    cout << "Palabra nro1: " << palabra1 << endl;
    cout << "Palabra nro2: " << palabra2 << endl;
    
    return 0;
}
