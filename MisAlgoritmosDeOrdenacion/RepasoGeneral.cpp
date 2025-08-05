#include <iostream>
using namespace std;

int main(){
    int aux,pos,x,n=5;
    int array[n]={1,5,8,3,9};

    //Seleccion directa

    /*for (int i=0;i<n;i++){
        aux=array[i];
        x=i;
        for(int j=i; j<n;j++){
            if(array[j]<aux){
                aux=array[j];
                x=j;
            }
        }
        array[x]=array[i];
        array[i]=aux;
    }*/

    //Burbuja
 
    /*for(int i=0; i<n;i++){
        for(int j=0;j<n;j++){
            if(array[j]>array[j+1]){
                aux=array[j];
                array[j]=array[j+1];
                array[j+1]=aux;
            }
        } 
    }*/

    //Insercion

   /*for(int i=0;i<n;i++){
    aux=array[i];
    pos=i;

    while(pos>0 && array[pos-1]>aux){
        array[pos]=array[pos-1];
        pos--;
    }

    array[pos]=aux;
   }*/

   //Insercion Intercambio

   for(int i=0; i<0; i++){
    pos=i;
    while(pos<0 && array[pos-1]>array[pos]){
        aux=array[pos];
        array[pos]=array[pos-1];
        array[pos-1]=aux;
        pos--;
    }
   }
   int numero, mitad,primero, ultimo;
   primero=0;
   ultimo=n-1;
   bool encontrado=false;
   cout << "Dame un numero" << endl;
   cin >> numero;

   while(primero<=ultimo && encontrado==false){
    mitad=(primero+ultimo)/2;
    if(array[mitad]==numero){
        cout << "Se encontro" << mitad << endl; 
        encontrado=true;
    }else if(array[mitad]<numero){
        primero=mitad+1;
    }else{
        ultimo=mitad-1;
    }
   }

    for(int i=0;i<n;i++){
        cout << array[i] << "\t";
    }
    cout << endl;
}