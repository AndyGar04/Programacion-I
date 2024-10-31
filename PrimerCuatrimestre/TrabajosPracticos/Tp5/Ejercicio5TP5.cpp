/* Desarrolla un programa que genere dos arreglos de tamaño 5 y los llene con números
aleatorios entre 3 y 57. Luego, crea un tercer arreglo del mismo tamaño donde cada elemento
sea la suma de los elementos correspondientes de los dos primeros arreglos. */

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
double PrimerArray[5],SegundoArray[5],TercerArray[5];


int main(){
     
    srand(time(NULL));

    for (int i=0; i<5;i++){
        PrimerArray[i] = rand() % 57 + 3;
        SegundoArray[i] = rand() % 57 + 3;
        TercerArray[i] = PrimerArray[i] + SegundoArray[i];
    }

        cout << "El Tercer arreglo recorrido es = [";
    for (int i=0;i<5;i++){
        cout << TercerArray[i] << " , ";
    }

    cout <<"]"<<endl;
}