/* Escribir un programa que realice la conversión de grados a radianes. Dato: PI = 180°.*/

#include <iostream>
#include <cmath>
using namespace std;

int main(){

  float grados;
  float trads; //Total Radianes

  cout << "Dame una cantidad de grados y lo pasare a radianes \n";
  cin >> grados;

  trads = (grados * M_PI) / 180;

  cout << "Los grados en radianes = ";
  cout << trads;

}