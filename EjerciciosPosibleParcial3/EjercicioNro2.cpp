/* Partiendo del siguiente arreglo desordenado:
5 53 900 54 306 2 99

a) Escribir un programa que permita ordenar un arreglo de mayor a menor (forma descendente) por el método
de ordenación por inserción.

b) Sin hacer código, mencionar en qué consiste el método de ordenación por inserción. ¿Cuál es la diferencia
con el método de ordenación por selección directa?

Si bien los metodos son de igual eficiencia, seleccion directa suele ser algo mejor, porque tiene menos
intercambios de posicion.

c) Sin hacer código, si ahora usted quiere buscar un elemento específico en el arreglo. Según lo
visto en la materia, mencione qué algoritmos de búsqueda podría implementar y cómo funcionan.
¿Cuáles son sus diferencias? ¿Cuál busca más rápido al elemento? ¿Por qué? 

Si en este momento y quisiera buscar en un arreglo ordenado, utilizaria la busqueda binaria ya que es la más rapida
sin embargo, en caso de querer buscar en un arreglo desordenado, utilizaria una busqueda convencional, que me
permita saber si hay algun elemento repetido, no sera la más rapida, pero sera certera.*/

#include <iostream>
using namespace std;

int main(){
    int pos,i,aux,n=7;
    int array[n]={5,53,900,54,306,2,99};
    
    for(i=1; i<n;i++){
        pos=i;
        aux=array[i];
        while(pos>0 && array[pos-1]<aux){
           array[pos]=array[pos-1];
           pos--;
        }
        array[pos]=aux;
    }
    
    for (int j=0; j<n; j++){
       cout << array[j] << "\t";
    }

    cout << endl;
}