#include <iostream>
using namespace std;

int main(){

    char letra;

    cout << "Dame una letra y te dire si es una vocal\n";
    cin >> letra;

    if (letra=='a' || letra=='e' || letra=='i' || letra=='o' || letra=='u'){
        cout << "La letra es vocal\n";
    }else{
        cout << "La letra no es vocal\n";
    }

 
}