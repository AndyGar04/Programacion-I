/*Hacer un programa en C++, para determinar el promedio de tres notas y determinar si el
estudiante aprobó o no.*/

#include <iostream>
using namespace std;

int main(){

   float promedio, nota1,nota2,nota3;

   cout << " Dame las tres notas al hilo \n";
   cin >> nota1;
   cin >> nota2;
   cin >> nota3;

   promedio=(nota1+nota2+nota3)/3;

   if (promedio>=6){
    cout << "El estudiante aprobo con " << promedio << endl;
   }else{
    cout << "El estudiante desaprobo con " << promedio << endl;
   }

}