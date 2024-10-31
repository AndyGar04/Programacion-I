/* Implementando subprogramas que devuelvan un resultado y errores que impidan realizar cálculos, 
escribir un programa que permita determinar si un número entero positivo es primo, el usuario deberá 
tener la posibilidad de ingresar por teclado el número.
Recordar: Los números primos son aquellos que solo son divisibles entre ellos mismos y el 1. */
#include <iostream>
using namespace std;

bool Errores(bool &Error,int numero);

int main(){
    int n, count=0;
    bool NotificacionDeError;

    cout << "Dame un numero entero positivo y te dire si es primo o no" << endl;
    cin >> n;

    if (Errores(NotificacionDeError, n) == false){
        return 0;
    }else{

     for(int i=1; i<n; i++){
        if ((n % i)==0){
         count++;
        }
     }
 
     if (count>2){
         cout << "El numero no es primo"<<endl;
     }else{
         cout << "El numero es primo"<<endl;
     }
    }
}

bool Errores(bool &Error,int numero){
    if (numero>0){
        Error = true;
    }else if(numero<=0){
        Error = false;
        cout << "Ingresaste un valor fuera de los parametros"<<endl;
    }
    return Error;
}