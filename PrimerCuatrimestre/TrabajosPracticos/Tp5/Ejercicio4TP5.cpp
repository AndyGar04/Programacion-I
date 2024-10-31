/* Desarrolla un programa que permita al usuario ingresar 5 valores para cada uno de dos
arreglos. Luego, debe crear un tercer arreglo que contenga la unión de los dos anteriores
ingresados por el usuario y lo muestre en consola. */

#include <iostream>
using namespace std;
double PrimerArray[5],SegundoArray[5],TercerArray[10];

int main(){
     
    for (int i=0; i<5;i++){
        cout << "Por favor cargue el primer arreglo" << endl;
        cin >> PrimerArray[i];
    }

    for (int i=0; i<5;i++){
        cout << "Por favor cargue el segundo arreglo" << endl;
        cin >> SegundoArray[i];
    }
    
    for (int i=0; i<5;i++){
        TercerArray[i] = PrimerArray[i];
        TercerArray[i+5] = SegundoArray[i];
    }

        cout << "El Tercer arreglo recorrido es = [";
    for (int i=0;i<10;i++){
        cout << TercerArray[i] << " , ";
    }

    cout <<"]"<<endl;
}