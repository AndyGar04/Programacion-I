/* 
1. Desarrolla un programa completo de control para un invernadero que permita administrar distintas partes 
del mismo. Utiliza un bucle para mostrar continuamente el menú y permitir al usuario seleccionar una opción. 
Utiliza la estructura switch para ejecutar la acción correspondiente según la opción seleccionada. Las 
opciones que deben figurar en el menú son:

-Controlar la temperatura: El usuario podrá ajustar la temperatura del invernadero dentro de un
 rango deseado (entre 17.9° y 24.5°).
-Controlar la iluminación: El usuario podrá regular la intensidad de la iluminación en el 
invernadero (desde 0 hasta 100 pasando solo por números enteros).
-Controlar el riego: El usuario modifica el estado de los riegos de encendido a apagado o al revés.
-Salir del programa: El usuario podrá finalizar el programa y salir.

Observaciones: Se debe modificar una variable de control en cada caso. 
*/

#include <iostream>
using namespace std;

int main(){
    double temperatura=0;
    int gradoIluminacion=0;
    int menu=0;
    int riesgo=0;

    do{
      cout << "1: Controlar temperatura" << endl;
      cout << "2: Controlador grado iluminacion" << endl;
      cout << "3: Ajustador de riesgo"<<endl;
      cout << "4: Salir"<<endl;
      cin >> menu;

      switch(menu){

        case 1:
        cout << "Dame un valor entre 17.9° y 24.5°"<<endl;
        cin >> temperatura;
        if (temperatura < 24.5 && temperatura > 17.9){
           cout << "Se establecio la temperatura"<<endl;
        }else{
          cout << "Temperatura incorrecta"<<endl;  
          temperatura=0;
        }
        menu=0;
        break;

        case 2:
        cout << "Ajuste la ilumniacion entre 0 y 100"<<endl;
        cin >> gradoIluminacion;
        if (gradoIluminacion >= 0 && gradoIluminacion <= 100){
           cout << "Se establecio la iluminacion"<<endl;
        }else{
          cout << "Ilumnacion incorrecta"<<endl;  
          gradoIluminacion=0;
        }
        menu=0;
        break;

        case 3:
        cout << "Escriba 1 para activar y 0 para desactivar " << endl;
        cin >> riesgo;
        if (riesgo == 0){
            cout << "Se desactivo"<< endl;
        }else if(riesgo == 1){
            cout << "Se activo"<< endl;
        }else{
            cout << "Ingresaste un valor invalido" << endl;
            riesgo=0; 
        }
        menu=0;
        break;

        default:
        cout << "Ingresaste un valor invalido" << endl;
        menu=0;
        break; 
        }
    }while(menu!=4);
}


