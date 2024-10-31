/* Crea un programa que pida al usuario ingresar las coordenadas (x, y) de dos puntos en un
plano cartesiano, y luego calcule e imprima en pantalla la distancia entre los dos puntos.*/

#include <iostream>
#include <cmath>
using namespace std;

int main(){

 float x0,x1,y0,y1,d;

 cout << "Dame y0 y x0 para calcular distancia" << endl;
 cin >> y0;
 cin >> x0;

 cout << "Dame y1 y x1 para calcular distancia" << endl;
 cin >> y1;
 cin >> x1;

 d = sqrt((pow((x1-x0),2)+pow((y1-y0),2)));

 cout << "La distancia es " << d << "um";
}