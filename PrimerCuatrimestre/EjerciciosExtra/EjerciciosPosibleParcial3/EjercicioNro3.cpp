/* Manejo de funciones:
Observación: Resuelva el ejercicio creando funciones que solo tengan un propósito. 
Por ejemplo: La función mostrar solo debe mostrar los campos del estudiante, por lo tanto, 
no debe contemplar ni hacer otra cosa. */


#include <iostream>
#include <string>

using namespace std;

/* Crea un programa que gestione una lista de estudiantes. Cada estudiante debe tener los siguientes atributos: 
nombre, edad, la nota de los 3 parciales (en un arreglo) y si aprobó o no. El programa debe permitirle al usuario
ingresar la cantidad de estudiantes que desee de a lista sin necesidad de ingresar la lista por completo, luego 
se debe mostrar todos los estudiantes ingresados, también se debe ver en terminal el porcentaje de aprobados 
del curso.*/

struct Estudiante {
    string nombre;
    int edad;
    double notas[3];
    bool aprobado;
};

int main() {
    int n;
    double promedio=0;
    cout << "Hola, dime la cantidad de estudiantes"<<endl;
    cin >> n;
    Estudiante Array[n];

    for (int i = 0; i < n; ++i) {
        cout << "Ingrese el nombre del estudiante " << i + 1 << ": ";
        cin >> Array[i].nombre;
        cout << "Ingrese la edad del estudiante " << i + 1 << ": ";
        cin >> Array[i].edad;
        for (int j = 0; j < 3; ++j) {
            cout << "Ingrese la nota " << j + 1 << " del estudiante " << i + 1 << ": ";
            cin >> Array[i].notas[j];
            promedio=promedio+Array[i].notas[j];
        }
        if ((promedio/3)>=6){
            Array[i].aprobado=true;
        }else{
            Array[i].aprobado=false;
        }  
        promedio=0;
    }

    // Se debe ver en terminal el porcentaje de aprobados del curso
    int countAprobados=0;
    for (int i = 0; i < n; ++i) {
        if ((Array[i].aprobado)==true){
            countAprobados++;
        }  
    }

   double porcentajeAprobados = (countAprobados / n) * 100;

    cout << "El porcentaje de aprobados es " << porcentajeAprobados << "%" << endl;
}

