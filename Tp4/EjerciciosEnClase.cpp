#include <iostream>
using namespace std;

int main(){

    int num = 1;

    while(num * num <= 1000){
        num++;
    }

    cout << "El primer numero cuyo cuadrado es mayor o igual que mil es "<<num<<endl;
}