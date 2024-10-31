/* Escribe un programa que le pida al usuario que ingrese 10 números y los almacene en un
arreglo. Luego, el programa debe calcular la suma de todos los elementos del arreglo y
mostrar el resultado */

#include <iostream>
using namespace std;
double array[10];
double total;

int main(){
     
    for (int i=0; i<10;i++){
        cout << "Por favor cargue el arreglo" << endl;
        cin >> array[i];
        total=total+array[i];
    }
    cout << "Todos los elementos del arreglos sumados da = " << total <<endl;
    cout << "El arreglo recorrido es = [";
    for (int i=0;i<10;i++){
        cout << array[i] << " , ";
    }

    cout <<"]"<<endl;
}