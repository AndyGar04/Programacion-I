#include <iostream>
using namespace std;

int main(){
    int i, j, menor, x, n=5;
    int array[n]={3,4,6,10,1};

    for (i=0; i<n-1; i++){
        menor=array[i]; //Toma el valor en la posicion i
        x=i; //Guarda el valor de la posicion
        for(j=i; j<n;j++){
           if(array[j] < menor){ //Si el valor de la posicion j es menor(O mayor) a menor entonces
            menor=array[j]; //Le damos el valor a de la posicion a menor
            x=j; //Guarda la posicion del menor
           }
        }
        array[x]=array[i]; //Pone en la posicion nro x el valor de la variable iterada
        array[i]=menor;  //Le damos el valor del menor, a la posicion actual
    }

    for(int i=0; i<n; i++){
        cout << array[i] << "\t";
    }

    cout << endl;
}