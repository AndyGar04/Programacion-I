#include <iostream>
using namespace std;

int main(){
    int aux,n=5;
    int array[n]={6,3,9,7,1};

    for (int i=0; i<n-1; i++){  //Primer for, encargado de iterar por cada posicion el arreglo
        for (int j=0; j<n-1;j++){ //Segundo for, encargado de obtener las posiciones para comparar
            if(array[j]>array[j+1]){ //Si el valor en la posicion actual es (menor o) mayor a la siguiente
                aux=array[j]; //Tomamos el valor de la posicion actual y lo guardamos en aux
                array[j]=array[j+1]; //Tomamos el valor de la posicion actual y le damos el valor de la siguiente
                array[j+1]=aux; //Igualamos la posicion siguiente a el valor de la posicion actual(Ahora posterior)
            }
        }
    } 

    for(int i=0; i<n; i++){
        cout << array[i] << "\t";
    }

    cout << endl;

}