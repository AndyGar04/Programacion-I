#include <iostream>
#include <cmath>
using namespace std;

int main(){

   double numerador, denominador, resultado;

   cout << "Dame un numerador \n";
   cin >> numerador;
   cout << "Dame un denominador \n";
   cin >> denominador;

   if (denominador == 0){
      cout << "¿Sos bobi o tratas de dividir por 0?\n";
   }else{
      resultado = numerador/denominador;
      cout << "El resultado es " << resultado << endl;
   }

}