/* Hacer un programa en C++, para ayudar a un trabajador a saber cuál será su sueldo
semanal, se sabe que, si trabaja 40 horas o menos, se le pagará $1000 por hora, pero si
trabaja más de 40 horas entonces las horas extras se le pagarán a $2000 por hora. */

#include <iostream>
using namespace std;

int main(){

    int horas;
    double totalPago;

    cout << "Dame la cantidad de horas trabajadas\n";
    cin >> horas;

    if (horas > 40){
        totalPago = 2000 * horas;
        cout << "Se le pagaran $2000 por hora\n";
    }else{
      totalPago= 1000 * horas;
      cout << "Se le pagaran $1000 por hora\n\n";
    }

    cout << "Le pagaran $" << totalPago << endl;

}