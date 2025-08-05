/* Hacer un programa en C++, para una tienda de helado da un descuento por compra a
sus clientes con membresía dependiendo de su tipo, sólo existen tres tipos de
membresía, tipo A, tipo B y tipo C. Los descuentos son los siguientes:
◦ Tipo A 10% de descuento
◦ Tipo B 15% de descuento
◦ Tipo C 20% de descuento */

#include <iostream>
using namespace std;

int main(){
  
  int Descuento;
  float Pago, PagoDescuento;

  cout << "¿Cual es el total a pagar sin descuento? \n";
  cin >> Pago;
  
  cout << "¿Cual es su membresia?\n"
  "1)Tipo A 10% de descuento \n"
  "2)Tipo B 15% de descuento\n"
  "3)Tipo C 20% de descuento\n";
  cin >> Descuento;

  switch(Descuento){
   case 1:
   {
    PagoDescuento=Pago-(Pago*0.1);
    cout << "El total a pagar es de " << PagoDescuento << endl; 
   } 
   break;
   case 2:
   {
    PagoDescuento=Pago-(Pago*0.15);
    cout << "El total a pagar es de " << PagoDescuento << endl; 
   }
   break;
   case 3:
   {
    PagoDescuento=Pago-(Pago*0.2);
    cout << "El total a pagar es de " << PagoDescuento << endl; 
   }
  }
}