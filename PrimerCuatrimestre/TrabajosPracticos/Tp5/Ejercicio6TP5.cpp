/* Escribe un programa que genere un arreglo de 8 lugares y lo llene con números aleatorios.
Luego, crea otro arreglo del mismo tamaño y llena este segundo arreglo con los valores del
primero, pero en orden inverso. Finalmente, muestra ambos arreglos en pantalla. */

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
double PrimerArray[8],SegundoArray[8];


int main(){
     
    srand(time(NULL));

    for (int i=0; i<8;i++){
        PrimerArray[i] = rand() % 57 + 3;
    }

    for (int i=8; i>=0;i--){
        SegundoArray[i] = PrimerArray[7-i];
    }

        cout << "El Primer arreglo recorrido es = [";
    for (int i=0;i<8;i++){
        cout << PrimerArray[i] << " , ";
    }

    cout <<"]"<<endl;

     cout << "El Segundo arreglo recorrido es = [";
    for (int i=0;i<8;i++){
        cout << SegundoArray[i] << " , ";
    }

    cout <<"]"<<endl;
}