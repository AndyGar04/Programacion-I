/*Escribir un programa que al ingresar las notas de los 3 parciales del curso, devuelva el
valor del promedio, el valor del promedio redondeado (“round”) y el valor del promedio
truncado (“trunc”).*/

#include <iostream>
#include <cmath>
using namespace std;

int main() {

  float Nota1, Nota2, Nota3, Promedio, PRound, Trunqueado;

  cout << "Dame las notas de los tres parciales \n";
  cin >> Nota1;
  cin >> Nota2;
  cin >> Nota3;

  Promedio = ((Nota1+Nota2+Nota3) / 3.0);
  PRound = round(Promedio);
  Trunqueado = trunc(Promedio);

  cout << "El promedio redondeado es " << PRound << endl;
  cout << "El promedio trunqueado es \n" << Trunqueado << endl;
  return 0;
}
