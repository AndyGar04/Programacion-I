/* Escribe un programa que solicite al usuario ingresar un número entero positivo. El
programa debe calcular la raíz cuadrada de este número y quedarse con la parte entera
del resultado. Luego, determina la cantidad de cifras que tiene el número ingresado.
Finalmente, eleva la parte entera de la raíz cuadrada a la cantidad de cifras y muestra este
resultado en pantalla. */

#include <iostream>
#include <cmath>
using namespace std;

int main(){

 double num, Rraiz, cifras, Resultado;
 int EntRaiz;

 cout << "Dame un numero\n";
 cin >> num;

 cifras = trunc(log10(num));

  if (num<0){
   cout << "No se puede hacer a raiz cuadrada de un numero negatio\n";
  }else{
   Rraiz=sqrt(num);
   Resultado=pow(int(Rraiz),(cifras+1));
   EntRaiz=int(Rraiz);
 
   cout << num << "-> Valor ingresado\n";
   cout << Rraiz << "-> Raiz cudrada\n";
   cout << EntRaiz << "-> Su Parte entera\n";
   cout << cifras << "-> Es el numero de cifras\n";
   cout << Resultado <<"-> Es el resultado\n";
  }
}