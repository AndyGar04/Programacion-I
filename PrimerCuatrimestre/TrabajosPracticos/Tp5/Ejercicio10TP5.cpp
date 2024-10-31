/* Escribir un programa que le permita al usuario ingresar la diagonal principal de una matriz
de 5x5 y que los otros lugares se completen con una X. */

#include <iostream>
using namespace std;

int main(){

 int num,num2,num3,num4,num5;
 
 cout << "Completa la diagonal principal uno a uno " << endl;
 cin >> num;
 cin >> num2;
 cin >> num3;
 cin >> num4;
 cin >> num5;

 for (int i = 0 ; i < 5 ; i++){
     for (int j = 0 ; j < 5 ; j++){
        if (i==0 && j==0){
            cout << " " << num << " ";
          }else if(i==1 && j==1){
                cout << " " << num2 << " ";
             }else if(i==2 && j==2){
                 cout << " " << num3 << " ";
              }else if(i==3 && j==3){
                  cout << " " << num4 << " ";
               }else if(i==4 && j==4){
                   cout << " " << num5 << " ";
                }else{
                    cout << " X ";
                }
        }
        cout << endl;
    }
  
}
