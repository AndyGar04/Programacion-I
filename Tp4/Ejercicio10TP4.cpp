/* Misma consigna que el ejercicio anterior pero ahora dejando los espacios del medio sin llenar.
Por ejemplo, al ingresar lado = 4, el dibujo debe quedar de la siguiente manera. */

#include <iostream>
using namespace std;

int main(){
    int Dim,DimP;
    cout << "Dame un numero y te hare un cuadrado de * de esa dimension"<<endl;
    cin >> Dim;

        for (int i = 0; i < Dim; i++) {
        for (int j = 0; j < Dim; j++) {
            if (i != Dim / 2 || j != Dim / 2) {
                cout << "* ";
            } else {
                cout << "  ";
            }
        }
        cout << endl;
    }
}
