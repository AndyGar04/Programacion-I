/* Escribe una función que tome un arreglo de enteros y lo ordene de mayor a menor.
• Inserción.
• Inserción con intercambios.
• Selección directa.
• Burbujeo. */
#include <iostream>
using namespace std;

void OrdenBurbujeo(int nums[], int c){
    int i,j,temp;
    for (i = 0; i < c-1; ++i){
        for (j = 0; j < c-1; ++j){
            if (nums[j] > nums[j+1]){
                temp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = temp;
            }
        }
    }
    cout << "Arreglo Ordenado: ";
    for (i = c-1; i > -1; --i){
        cout<< nums[i] <<" ";
    }
    cout << endl;
}

void OrdenSeleccionDirecta(int nums[], int c){

 int i,j,x,menor;
    for (i = 0; i < c-1; ++i){
        menor = nums[i];
        x = i;
        for (j = i; j < c; ++j){
            if (nums[j] > menor){
                menor = nums[j];
                x = j;
            }
        }
        nums[x] = nums[i];
        nums[i] = menor;
    }

    cout << "Arreglo Ordenado : ";

    for (i = 0; i < c; ++i){
        cout << nums[i] << " ";
    }

    cout << endl;

}

void OrdenInsercionIntercambios(int nums[], int c){
    int pos, tmp;
    //ALGORITMO DE ORDENAMIENTO POR INSERCION CON INTERCAMBIOS
    for (int i = 0; i < c; i++){
        pos=i;
        while ((pos >0 ) && (nums[pos-1] < nums[pos]))
        {
            //INTERCAMBIAMOS CON LA VARIABLE TEMPORAL
            tmp = nums[pos];
            nums[pos] = nums [pos - 1];
            nums [pos - 1]=tmp;
            pos--;
        }
    }
    //IMPRIMO EN ORDEN ASCENDENTE ORDENADO !
    cout<<"Arreglo Ordenado : ";
    for (int j=0; j< c; j++)
    {
       cout<< nums[j] <<" "; 
    }

    cout << endl;

}

void OrdenInsercion(int nums[], int c) {
    int pos, aux;

    // ALGORITMO DE ORDENAMIENTO POR INSERCION
    for (int i = 1; i < c; i++) { // Empezamos desde 1 porque el primer elemento ya está "ordenado"
        pos = i;
        aux = nums[i]; // Almacena el valor actual

        // Orden descendente
        while (pos > 0 && nums[pos - 1] < aux) { // nums[pos-1] < aux para descendente
            nums[pos] = nums[pos - 1];
            pos--;
        }
        nums[pos] = aux;
    }

    // IMPRIMO EN ORDEN DESCENDENTE ORDENADO
    cout << "Arreglo Ordenado: ";
    for (int j = 0; j < c; j++) {
        cout << nums[j] << " ";
    }
    cout << endl;
}

int main(){

    int n = 5;
    int numeros[] = {5, 3, 1, 2, 4}; // ARREGLO DESORDENADO
    cout << "Arreglo por insercion" << endl;
    OrdenInsercion(numeros, n);
    cout << "Arreglo de insercion por intercambios" << endl;
    OrdenInsercionIntercambios(numeros, n);
    cout << "Arreglo por seleccion directa " << endl;
    OrdenSeleccionDirecta(numeros, n);
    cout << "Arreglo por metodo burbuja " << endl;
    OrdenBurbujeo(numeros,n);
}
