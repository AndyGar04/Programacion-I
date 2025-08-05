/* Escriba un programa que solicite al usuario el valor de un ángulo en grados, y muestre en
pantalla su valor en radianes. Si el valor ingresado es mayor que 360, el programa debe
calcular cuantas vueltas dió (1 vuelta = 360°) y en qué cuadrante se encuentra dicho ángulo.
Si es menor que 360° que calcule el seno, coseno y tangente de dicho ángulo */

#include <iostream>
#include <cmath>
using namespace std;

int main(){
    float grados, radianes, vueltas, restos;

    cout << "Dame un angulo en grados" << endl;
    cin >> grados;

    radianes = grados * (M_PI/180);

    cout << "El valor ingresado en radianes es " << radianes << endl;

    if (grados > 360){
        vueltas = grados / 360.0;
        restos = vueltas - grados / 360.0;
        cout << vueltas << " es el numero de vueltas" << endl;

        if (restos <= 0.25){
            cout << "Superior derecho" << endl; 
        }else if(restos <= 0.50){
            cout << "Superior izquierdo" << endl;
        }else if(restos <=0.75){
            cout << "Inferior izquierdo" << endl;
        }else{
            cout << "Inferior derechi" << endl;
        }
    }else{
        cout << "El coseno es " << cos(radianes) << endl;
        cout << "La tangente es " << tan(radianes) << endl;
        cout << "El seno es " << sin(radianes) << endl;
    }
}

