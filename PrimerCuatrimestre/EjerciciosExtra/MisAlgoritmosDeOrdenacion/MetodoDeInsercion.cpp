#include <iostream>
using namespace std;


int main(){
    int aux, pos, n=6;
    int array[n]={5,7,3,19,20,9};

    for(int i=1;i<n;i++){
        pos=i;                  //Definimos la posicion actual.     
        aux=array[i];          //Guardamos en aux el dato de la posicion actual.

        while(pos>0 && array[pos-1]>aux){ //Si posicion no es 0 y la posicion anterior es mayor (o menor) de aux
            array[pos]=array[pos-1];  //Intercambiamos posicion
            pos--;                   //Decrementamos la posicion para poder seguir ordenando
        }
        //Salida del bucle while
        array[pos]=aux; //Recuperamos el dato anteriormente guardado en aux
    }

    for (int i=0; i<n; i++){
        cout << array[i] << "\t";
    }

    cout << endl;

}