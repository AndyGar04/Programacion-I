#include <iostream>
using namespace std;

int main(){

 int fila = 3;
 int col = 3;

 int Matriz[fila][col];
 
 for (int i = 0 ; i < fila ; i++){
     for (int j = 0 ; j < col ; j++){
         Matriz[i][j] = i * 10 + j;
     }
    }

 for (int i = 0 ; i < fila ; i++){
     for (int j = 0 ; j < col ; j++){
         cout << Matriz[i][j] << " ";
     }
     cout << endl;
    }

}