#include <iostream>
using namespace std;

void MetodoSeleccionDirecta(int array[], int n);
void MetodoInsercion(int array[], int n);
void MetodoInsercionPorIntercambio(int array[], int n);
void MetodoBurbuja(int array[], int n);
void BusquedaBinaria(int array[], int n);

int main(){
    int d=5;
    int a[d]={5,8,2,9,10};
    //MetodoSeleccionDirecta(a,d);
    //MetodoInsercion(a,d);
    //MetodoInsercionPorIntercambio(a,d);
    MetodoBurbuja(a,d);
    BusquedaBinaria(a,d);
    for (int i=0; i<d; i++){
        cout << a[i] << "\t";
    }
    cout << endl;
}

void MetodoSeleccionDirecta(int array[],int n){
    int menor, x, i, j;
    for (i=0;i<n;i++){
       x=i;
       menor=array[i];
       for (j=i;j<n;j++){
        if(array[j]<menor){
            menor=array[j];
            x=j;
        }
       }
       array[x]=array[i];
       array[i]=menor;
    }
}

void MetodoInsercion(int array[], int n){
    int aux,pos;

    for (int i=0; i<n; i++){
       pos=i;
       aux=array[i];
       while(pos>0 && array[pos-1]>aux){
        array[pos]=array[pos-1];
        pos--;
       }
        array[pos]=aux;
    } 
    
}

void MetodoInsercionPorIntercambio(int array[], int n){
    int pos, aux;

    for (int i=0; i<n; i++){
        pos=i;
        while(pos>0 && array[pos-1]>array[pos]){
            aux=array[pos];
            array[pos]=array[pos-1];
            array[pos-1]=aux;
            pos--;
        }
    }
}

void MetodoBurbuja(int array[], int n){
    int aux;

    for(int i=0; i<n-1; i++){
        for(int j=0; j<n-1; j++){
            if (array[j]>array[j+1]){
                aux=array[j];
                array[j]=array[j+1];
                array[j+1]=aux;
            }
        }
    }
}

void BusquedaBinaria(int array[], int n){
    int primero, ultimo, mitad, numero;
    bool Encontrado=false;
    primero=0;
    ultimo=n-1;
    cout << "Dame un numero " << endl;
    cin >> numero;
    while(Encontrado==false && primero <= ultimo){
        mitad=(primero+ultimo)/2;
        if(array[mitad]==numero){
            cout << "Se encontro en la posicion " << mitad << endl;
            Encontrado=true;
        }else if(numero < array[mitad]){
            ultimo=mitad-1;
        }else{
            primero=mitad+1;
        }
    }

    if (Encontrado==false && primero>=ultimo){
        cout << "No se encontro" << endl;
    }
}