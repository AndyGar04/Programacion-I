/* 9) Implementa una función llamada "quitarVocales" que reciba una cadena de caracteres y
elimine todas las vocales de la palabra, manteniendo el resultado en la misma variable. */
#include <iostream>
#include <string>
using namespace std;

string QuitarVocales(string palabrilla){
    for (int i = 0; i < palabrilla.length(); i++) {
        if (palabrilla[i] == 'a' || palabrilla[i] == 'e' || palabrilla[i] == 'i' || palabrilla[i] == 'o' ||
            palabrilla[i] == 'u' || palabrilla[i] == 'A' || palabrilla[i] == 'E' || palabrilla[i] == 'I' ||
            palabrilla[i] == 'O' || palabrilla[i] == 'U') {
            palabrilla[i] = ' ';
        }
    }
    return palabrilla;
}

int main() {
    string palabra;
    cout << "Dame una palabra: " << endl;
    cin >> palabra;

    palabra = QuitarVocales(palabra);

    cout << palabra << endl;
}
