/* Calcular el valor del coseno, seno y tangente de un ángulo (entero) en grados, ingresado
por el usuario. Recuerde que las funciones “cos”, “sin” y “tan” trabajan con ángulos en
radianes.*/

#include <iostream>
#include <cmath>
using namespace std;

int main(){

  float grados, trads, coseno, tangente, seno; //Grados, TotalRadianes, Coseno, Tan y Seno

  cout << "Dame una cantidad de grados \n";
  cin >> grados;

  trads = (grados * M_PI) / 180;

  coseno = cos(trads);
  tangente = tan(trads);
  seno = sin(trads);

  cout << "El coseno es = ";
  cout << coseno << endl;
  cout << "El seno es = ";
  cout << seno << endl;
  cout << "La tangente es = ";
  cout << tangente << endl;

}