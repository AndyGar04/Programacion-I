#include <iostream>
using namespace std;

int main(){
    int numero, mitad, primero, ultimo,x,n=7;
    int array[n]={1,2,3,4,5,6,7,8};
    primero=0;
    ultimo=n-1;
    x=-1;
    cout << "Dame un numero y lo buscare"<<endl; 
    cin >> numero;
    while (primero <= ultimo && x==-1){ //Primero debe ser menor o igual a ultimo
        mitad=(primero+ultimo)/2; //Calculamos la mitad
        if (numero==array[mitad]){ //Si es igual, terminamos la ejecucion
            cout << "Se encontro en la posicion " << mitad;
            x=1;
        }else if(numero < array[mitad]){ //Si es menor, esta en la mitad de más pequeño
           ultimo=mitad-1; //Acortamos el orden de busqueda
        }else{ //Si es mayor, es porque esta en la mitad mas grande
            primero=mitad+1; //Acortamos el orden de busqueda
        }
    }

}