/* Implementa una función que reciba una estructura "Persona" (con campos como nombre,
edad, etc.) por valor y la imprima en pantalla. */

#include <iostream>
#include <string>
using namespace std;

struct Persona{
   string nombre, nacionalidad;
   int edad;
};

void LeerPersona(Persona P){
   cout << "Nombre: " << P.nombre << endl;
   cout << "Nacionalidad: " << P.nacionalidad << endl;
   cout << "Edad: " << P.edad << endl;
}

int main(){
    Persona Persona;
    cout << "Dame el nombre: ";
    cin >> Persona.nombre;
    cout << "Dame tu nacionalidad: ";
    cin >> Persona.nacionalidad;
    cout << "Dame tu edad: ";
    cin >> Persona.edad;
    LeerPersona(Persona); 
}