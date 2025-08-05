/* Escribir un programa que cuando el usuario ingrese los catetos de un triángulo rectángulo,
calcule y muestre en consola el valor de la hipotenusa. (Teorema de Pitágoras) */

#include <iostream>
#include <cmath>
using namespace std;

int main(){

  float Cat1, Cat2, Hip;

  cout << "Dame los dos catetos y te dare la hipotenusa de un triangulo rectangulo \n";
  cin >> Cat1;
  cin >> Cat2;
   
  if (Cat1 < 0 || Cat2 < 0) {
     cout << "Error, no se puede calcular con lados negativos";
  }else{
     Hip = sqrt(pow(Cat1,2) + pow(Cat2,2));
     cout << "La hipotenusa es " << Hip << " um";
  }
   
  return 0;
}
