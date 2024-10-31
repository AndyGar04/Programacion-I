/* Escribir un programa que calcule la suma de los primeros n números naturales utilizando un
bucle while */

#include <iostream>
using namespace std;

int main(){

  int n, cont, suma;
  cont = 0;
  suma = 0;

  cout << "Dame un numero y te dare la suma de sus anteriores\n";
  cin >> n;

  while (cont < n){
    cont++;
    suma=suma+cont;
  }

  cout << "La suma da " << suma <<endl;

}