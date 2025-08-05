/* 1)Escribir un programa que calcule la raíz cuadrada de un número ingresado por el usuario.
Tener en cuenta que no puede ser un número negativo, por lo tanto, solucionar ese
problema usando alguna función de <cmath>.*/

#include <iostream>
#include <cmath>
using namespace std;

int main(){

  float num;
  float raiz;

  cout << "Ingrese un numero positivo y te dare su raiz \n";
  cin >> num;

  if (num<0){
      cout << "El numero ingresado no es positivo \n";
  }else{
    raiz = sqrt(num);
    cout << "El resultado es = ";
    cout << raiz;
  }
}