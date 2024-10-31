//6) Estructuras y manejo de arreglos

#include <iostream>
#include <string>
//gordo puto
using namespace std;

/*  Crea una estructura "Estudiante" con los campos "nombre", "edad" y "notas" (este
campo debe almacenar la nota de los 3 parciales). Crea un arreglo de estructuras de
tamaño 3  puto y permite que el usuario ingrese los datos de los estudiantes. */

struct Estudiante {
    string nombre;
    int edad;
    double notas[3];
};

int main() {
    int n = 3;
    Estudiante Array[3];

    for (int i = 0; i < n; ++i) {
        cout << "Ingrese el nombre del estudiante " << i + 1 << ": ";
        cin >> Array[i].nombre;
        cout << "Ingrese la edad del estudiante " << i + 1 << ": ";
        cin >> Array[i].edad;
        for (int j = 0; j < 3; ++j) {
            cout << "Ingrese la nota " << j + 1 << " del estudiante " << i + 1 << ": ";
            cin >> Array[i].notas[j];
        }
    }

    // b) Mostrar la nota más alta de cada estudiante de forma clara
    for (int i = 0; i < n; ++i) {
        double maxNota = Array[i].notas[0];
        for (int j = 1; j < 3; ++j) {
            if (Array[i].notas[j] > maxNota) {
                maxNota = Array[i].notas[j];
            }
        }
        cout << "La nota más alta del estudiante " << Array[i].nombre << " es: " << maxNota << endl;
    }

    // c) Calcular y mostrar el promedio de cada alumno y el promedio general del curso.
    double promedioGeneral = 0;
    for (int i = 0; i < n; ++i) {
        double sumaNotas = 0;
        for (int j = 0; j < 3; ++j) {
            sumaNotas += Array[i].notas[j];
        }
        double promedio = sumaNotas / 3.0;
        cout << "El promedio del estudiante " << Array[i].nombre << " es: " << promedio << endl;
        promedioGeneral += promedio;
    }
    promedioGeneral /= n;
    cout << "El promedio general del curso es: " << promedioGeneral << endl;

    /* d) Modificar la nota del tercer parcial del segundo estudiante. Si tiene una nota menor que
       60, se le debe sumar el 25%, si la nota está entre 60 y 80 se le debe sumar el 5% y si es
       mayor que 80 debe restar el 3%. */

    cout << "La nota del tercel parcial del segundo estudiante es " << Array[1].notas[2] << endl;  

    if (Array[1].notas[2] > 80){
       Array[1].notas[2]= Array[1].notas[2]-Array[1].notas[2]*0.03;
       cout << "La nota fue modificada a " << Array[1].notas[2] << endl;
    }else if(Array[1].notas[2]<80 && Array[1].notas[2]>60){
      Array[1].notas[2]= Array[1].notas[2]+Array[1].notas[2]*0.05;
      cout << "La nota fue modificada a " << Array[1].notas[2] << endl;
    }else{
      Array[1].notas[2]= Array[1].notas[2]+Array[1].notas[2]*0.25;
      cout << "La nota fue modificada a " << Array[1].notas[2] << endl;
    } 

}

