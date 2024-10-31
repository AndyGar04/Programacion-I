/* Escribir un programa que calcule el valor de a, c y β. Sabiendo que y γ = 60°  
Alpha + Beta + γ = 180° y b=4 a b como opuesto SOHCAHTOA*/

#include <iostream>
#include <cmath>
using namespace std;

int main(){
    
    const float Alpha = 90;
    const float V = 60;
    const float b = 4;
    float Tang, Seno, Beta, a, c;

    Beta=180-Alpha-V;

    Tang = tan((60 * M_PI)/180);
    Seno = sin((60 * M_PI)/180);

    a = b/Tang;
    c = b/Seno;

    cout << "a = " << a << endl;
    cout << "c = " << c << endl;
    cout << "Beta = " << Beta << endl;
    
    return 0;
}

