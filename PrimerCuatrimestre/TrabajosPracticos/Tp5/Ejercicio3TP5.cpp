/*Escribe un programa que genere un arreglo de 8 elementos, llenándolo con números aleatorios
del 1 al 10. Luego, el programa debe encontrar y mostrar los valores mayor y menor del
arreglo. Además, contar y mostrar cuantas veces se repiten en el arreglo.*/


#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
double array[10];
double Menor=10;
double Mayor=0;
int count=0;

int main(){

    srand(time(NULL)); 
     
    for (int i=0; i<7;i++){
        cout << "Por favor cargue el arreglo" << endl;
        array[i] = rand() % 10 + 1;
    }
    
    for (int i=0; i<7;i++){
        if (array[i] > Mayor){
            Mayor = array[i];
        }else if (array[i] < Menor){
            Menor = array[i];
        }else{
            count++;
        }
    }

    cout << "El numero mas chico fue " << Menor << endl;
    cout << "El numero mas grande fue " << Mayor << endl;

    cout << "Se repiten " << count << endl;

    cout << "El arreglo recorrido es = [";
    for (int i=0;i<7;i++){
        cout << array[i] << " , ";
    }

    cout <<"]"<<endl;

}