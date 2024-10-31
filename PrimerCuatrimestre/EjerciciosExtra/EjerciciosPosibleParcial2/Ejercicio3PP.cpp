#include <iostream>
using namespace std;

int main(){

 int numero, contador=0; 
 int array[10];
 bool correcto=false;

  /*a) Primero, el usuario deberá introducir un número entero mayor que 0 y menor que 100. 
  Si esto no sucede, se le deberá indicar al usuario que "introduzca un número mayor que 0 
  y menor que 100". Hasta que no se ingrese un valor correcto entre esos rangos de valores, 
  el programa no continuará. Mostrar el valor en terminal.:*/

 do{
    cout << "Introduzca un numero mayor que 0 y menor 100" <<endl;
    cin >> numero;

    if (numero<100 && numero>0){
       cout << "El numero ingresado fue " << numero << endl;
       correcto = true;
    }else{
        cout << "Ingresaste erroneamente el numero " << numero << endl;
        correcto = false;
    }
 }while(correcto == false);

 /* b) Suponiendo que el usuario introdujo un número entero mayor que 0 y menor que 100 de manera correcta:
 -Escribir la parte del código que permite incrementar el índice del bucle de diez en diez hasta el valor máximo en cuestión que es 100. Mostrar el valor del índice en la terminal.
 Lo que veríamos en consola: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100.*/
  for (int i=1; i<=10; i++){
    cout << i * 10 << ", ";
  }
  cout << endl;
 /*-Utilizando el código anterior, se deberá implementar un arreglo llamado "arreglo" de tamaño 10. Entonces,
  cada valor se debe sumar los números en saltos de diez y mostrar en la terminal. Estos valores deberán 
  guardarse en el arreglo. Mostrar los valores en la terminal.
  arreglo: [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ] */

  for (int i=0; i<10; i++){
     array[i]=(i+1)*10;
     cout << array [i] << ", ";
   }

  cout << endl;

  /*c) En terminal, se deberá mostrar el resultado final de la suma de todos los valores del índice. 
  Entonces, se deberá mostrar el resultado final de la suma de todos los valores del índice:
  Lo que veríamos en consola: "La suma total del contador saltando en diez posiciones hasta 100 es: 550" */
  
  for (int i=0; i<10; i++){
     contador=contador + array[i];
   }
   cout << endl;
   cout << "La suma de estos valores da " << contador << endl;
}