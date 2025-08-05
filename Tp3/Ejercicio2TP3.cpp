#include <iostream>
using namespace std;

int main(){

    int num1,num2,num3;

    cout << "Dame tres numeros y te dire cual es el mayor\n";
    cin >> num1;
    cin >> num2;
    cin >> num3;

    if (num1>num2 && num1>num3){
        cout << num1 << " es el mayor.\n";
    }else if(num2>num3){
        cout << num2 << " es el mayor.\n";
    }else{
        cout << num3 << " es el mayor.\n";
    }


}