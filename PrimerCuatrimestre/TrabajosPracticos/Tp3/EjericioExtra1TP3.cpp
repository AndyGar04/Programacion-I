/*Escriba un programa que solicite al usuario dos números enteros y los intercambie si el
primero es mayor que el segundo. Luego, muestre en pantalla los valores de ambos números.*/

#include <iostream>
using namespace std;

int main(){

    int num1, num2, aux;

    cout << "Dame dos numeros\n";
    cin >> num1;
    cin >> num2;

    if (num1>num2){
        aux = num2;
        num2 = num1;
        cout << "Invertido serian...\n";
        cout << aux << endl;
        cout << num2 << endl;
    }else{
        cout << "El segundo fue igual o menor al segundo";
    }

}
