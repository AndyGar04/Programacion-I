/* Hacer un programa en C++, para una tienda de zapatos que tiene una promoción de
descuento para vender al mayor, esta dependerá del número de zapatos que se compren.
Si son más de diez, se les dará un 10% de descuento sobre el total de la compra; si el
número de zapatos es mayor de veinte, pero menor de treinta, se le otorga un 20% de
descuento; y si son más treinta zapatos se otorgará un 40% de descuento. El precio de
cada zapato es de $8000. */

#include <iostream>
using namespace std;

int main(){

    int pares;
    double totalPagar;

    cout << "Dame la cantidad de pares\n";
    cin >> pares;

    if (pares > 30){
        totalPagar= 8000 * pares - (8000 * pares)*(0.4);
        cout << "Descuento 40%\n";
    }else if (pares > 20){
      totalPagar= 8000 * pares - (8000 * pares)*(0.2);
      cout << "Descuento 20%\n";
    }else{
      totalPagar= 8000 * pares - (8000 * pares)*(0.1);
      cout << "Descuento 10%\n";
    }

    cout << "El total a pagar " << totalPagar << endl;

}