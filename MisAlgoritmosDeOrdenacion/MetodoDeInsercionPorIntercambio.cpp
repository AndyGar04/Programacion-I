#include <iostream>
using namespace std;

int main(){
    int aux, pos,n=8;
    int array[n]={0,1,5,2,6,3,8,60};

    for(int i=0; i<n; i++){
        pos=i;   //Guardamos la posicion
        while(pos>0 && array[pos-1]>array[pos]){ //Mientras pos sea mayor a 0 y la posicion aterior se mayor(o menor)
            aux=array[pos]; //Guardamos el valor en aux
            array[pos]=array[pos-1]; //Le damos el valor de la posicion anterior
            array[pos-1]=aux; //Le damos el valor de aux en a posicion anterior intercambiandolo
            pos--;//Decrementamos el valor de pos
        }
    }
    for(int i=0;i<n;i++){
        cout <<array[i]<<"\t";
    }
    cout<<endl;
}