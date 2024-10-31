/* Escribe un programa que ingrese 10 números y los almacene en un arreglo, estos deben ser
24, 5, 58, 100, 0, -8, 94, 96, -16, 105}. Luego, el programa debe pedirle al usuario que
ingrese un número para buscar en el arreglo. Si el número se encuentra en el arreglo, el
programa debe mostrar la posición en la que se encuentra. Si el número no está en el arreglo,
el programa debe mostrar un mensaje indicando que no se encontró.  */


#include <iostream>
using namespace std;
double array[10];
double buscador=0;
bool encontro = false;

int main(){
     
    for (int i=0; i<10;i++){
        cout << "Por favor cargue el arreglo" << endl;
        cin >> array[i];
    }
    
    cout << "Dame un numero y lo busco en el arreglo" << endl;
    cin >> buscador;
        
    for (int i=0;i<10;i++){
     if (buscador == array[i]){
       cout << "Se encontro en la posicion " << i+1 << endl; 
       encontro = true;    
     }
    }

    if(encontro == true){
        cout << "Se encontro!"<<endl;
    }else{
        cout << "No se encontro"<< endl;
    }
}