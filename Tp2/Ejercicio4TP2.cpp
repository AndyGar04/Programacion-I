/* Escribir un programa que calcule el perímetro y el área de un círculo, dependiendo del
radio que ingrese el usuario. */


#include <iostream>
#include <cmath>
using namespace std;

int main(){

  float radio, perimetro;

  cout << "Dame el radio y calculare el perimetro \n";
  cin >> radio;

  perimetro = (M_PI * pow(radio,2));

  cout << "El perimetro es "<< perimetro << " um";
  return 0;
}