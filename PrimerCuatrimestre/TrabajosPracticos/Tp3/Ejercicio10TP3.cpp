/*Mediante programación c++, crea una calculadora haciendo uso de la estructura de control condicional
Switch (Sumar, restar, multiplicar y dividir).*/

#include <iostream>
#include <cmath>
using namespace std;

int main(){

   int menu;
   double num1, num2, resultado;
   cout << "¿Que quieres hacer?\n"
             << "1) Sumar \n"
             << "2) Restar \n"
             << "3) Dividir \n"
             << "4) Multiplicar \n"
             << " Culaquier otro numero para salir \n";
    cin >> menu;       

 switch (menu){
    case 1:
     cout << "Dame dos numeros y los sumare\n";
     cin >> num1;
     cin >> num2;
     resultado=num1+num2;
     cout << "El resultado de la suma es " << resultado << endl;
    break; 
    case 2:
     cout << "Dame dos numeros y los restare\n";
     cin >> num1;
     cin >> num2;
     resultado=num1-num2;
     cout << "El resultado de la resta es " << resultado << endl;
    break; 
    case 3:
     cout << "Dame el numerador" << endl;
     cin >> num1;
     cout << "Dame el denominador" << endl;
     cin >> num2;
      if (num2==0){
         cout << "No se puede dividir por cero" << endl;
      }else{
       resultado=num1/num2;
       cout << "El resultado de la divicion es " << resultado << endl;
      }
    break; 
    case 4:
     cout << "Dame dos numeros y los multiplicare";
     cin >> num1;
     cin >> num2;
     resultado=num1*num2;
     cout << "El resultado de la multiplicacion es " << resultado << endl;
    break; 
    default:
     cout << "Saliste" << endl; 
    break;
   }
}